from collections import OrderedDict
from docutils.utils import column_width
from secret import FLASK_DIR
import yaml
import re
import os
import jinja2
import zlib

BASE_DIR = 'anime-sheet-music'

known_slugs = ['hackgu-vol-2', 'hackgu-vol-3', 'cosmo-warrior-zero', 'hackgu-vol-1', 'gedo-senki-tales-from-earthsea', 'ayumi-hamasaki', 'kingdom-hearts-utada-hikaru', 'kingdom-hearts-ii-utada-hikaru', 'hacksign', 'hackgame-infection-mutation-outbreak-quarantine', 'final-fantasy-ii', 'naruto', 'wild-arms', 'within-temptation', 'final-fantasy-viii', 'hackroots', 'hackliminality', 'death-note', 'princess-mononoke', 'nobuta-wo-produce', 'yui', 'granado-espada', 'taiyou-no-uta-erika-sawajiri', 'orisinal', 'always-sanchoume-no-yuuhi', 'xenogears-light', 'phoenix-wright-trials-and-tribulations', 'summon-night-ex-thesis-yoake-no-tsubasa', 'suzumiya-haruhi-no-yuuutsu-the-melancholy-of-haruhi-suzumiya', 'ghost-in-the-shell-stand-alone-complex', 'touhou-koumakyou-the-embodiment-of-scarlet-devil', 'cardcaptor-sakura', 'bludgeoning-angel-dokuro-chan', 'pokemon-gold-silver', 'pokemon-red-blue', 'hacklink', 'canvas-piano-collection-nao-plays-piano-', 'pokemon-black-white', 'the-legend-of-zelda-ocarina-of-time', 'relaxing-piano-wedding-songs', 'hackgu-trilogy', 'eve-no-jikan', 'spirited-away', 'ookami-kodomo-no-ame-to-yuki', 'one-ok-rock', 'utawarerumono', 'cowboy-bebop', 'tsubasa-reservoir-chronicle', 'zankyou-no-terror-terror-in-resonance', 'madlax', 'acca']

def get_slug(name):
    replacements = OrderedDict([('ō', 'ou'), ('ū', 'uu'), ('é', 'e'), ('λ', 'lambda'), (r'[^a-z0-9- ]', ''), (' ', '-'), (r'-+', '-'), ('^-', '')])
    slug = name.lower()
    for token in replacements:
        slug = re.sub(token, replacements[token], slug)
    return slug

with open('anime-sheet-music.yml') as f:
    sheets = yaml.load(f)

sections = set()
related = {}
for sheet_id in sheets:
    section, nom = sheets[sheet_id]['section'], sheets[sheet_id]['nom']
    sheets[sheet_id]['section_slug'] = get_slug(section)
    sheets[sheet_id]['nom_slug'] = get_slug(nom)
    related.setdefault(section, []).append((nom, sheets[sheet_id]['nom_slug']))

db = {}
for _, sheet in sheets.items():
    assert sheet['section_slug'] in known_slugs
    directory = os.path.join(BASE_DIR, sheet['section_slug'])
    sheet['h1_nom_row'] = '-' * column_width(sheet['nom'] + ' sheet music')
    sheet['h1_section_row'] = '-' * column_width(sheet['section'])
    sheet['h2_row'] = '=' * (column_width('Also from ' + sheet['section']))
    sheet['related_sheets'] = related[sheet['section']]
    slug = sheet['nom_slug']
    db[slug] = ['_static/sheets/%s.pdf' % sheet['lien'], '_static/sheets/%s.mid' % sheet['lien']]
    if sheet['lienrpgsoluce']:
        db[slug].append(sheet['lienrpgsoluce'])
    for i in range(len(db[slug])):
        with open(os.path.join(FLASK_DIR, 'stats', '%d.log' % zlib.adler32(bytes(db[slug][i], 'utf-8'))), 'w') as hits:
            counter_name = ['nbtelpdf', 'nbtelmid', 'nbtelrpg'][i]
            hits.write(str(sheet[counter_name]))

    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(os.path.join(directory, 'index.rst')):
        with open(os.path.join(directory, 'index.rst'), 'w') as f:
            f.write(jinja2.Template(open('_templates/section.rst').read()).render(**sheet))
    with open(os.path.join(directory, '%s.rst' % sheet['nom_slug']), 'w') as f:
        f.write(jinja2.Template(open('_templates/sheet.rst').read()).render(**sheet))
sheet_list_template = jinja2.Template(open('_templates/sheet-list.rst').read())

with open(os.path.join(BASE_DIR, 'top.rst'), 'w') as f:
    f.write(sheet_list_template.render(mode='Top', description='is ordered by decreasing popularity', sheet_list=sorted(sheets.values(), key=lambda x: -x['nbtelpdf'])))

with open(os.path.join(BASE_DIR, 'latest.rst'), 'w') as f:
    f.write(sheet_list_template.render(mode='Latest', description='is ordered by decreasing last update', sheet_list=sorted(sheets.values(), key=lambda x: x['date2'], reverse=True)))

with open(os.path.join(BASE_DIR, 'youtube.rst'), 'w') as f:
    f.write(sheet_list_template.render(mode='YouTube-only', description='contains only sheet music with a recorded YouTube video', sheet_list=sorted(filter(lambda x: x['youtube'], sheets.values()), key=lambda x: (x['section'], x['nom']))))

with open(os.path.join(BASE_DIR, 'piano.rst'), 'w') as f:
    f.write(sheet_list_template.render(mode='Piano-only', description='contains only piano sheet music', sheet_list=sorted(filter(lambda x: x['instruments'] == 'Piano', sheets.values()), key=lambda x: (x['section'], x['nom']))))

with open(os.path.join(BASE_DIR, 'piano-voice.rst'), 'w') as f:
    f.write(sheet_list_template.render(mode='Piano & Voice-only', description='contains only piano & voice sheet music', sheet_list=sorted(filter(lambda x: x['instruments'] == 'Piano, Voice', sheets.values()), key=lambda x: (x['section'], x['nom']))))

with open(os.path.join(FLASK_DIR, 'db.py'), 'w') as f:
    f.write('SHEETS = {\n')
    for slug in db:
        f.write('    "%s": %s,\n' % (slug, db[slug]))
    f.write('}')
