import re
import os

link = re.compile(r'- `(.*) <(.*)>`_')

with open('tp/index.rst') as f:
    for line in f:
        m = link.match(line)
        if m:
            title, url = m.groups()
            if url.endswith('pdf'):
                last_subject = '- `%s <%s>`_' % (title, url)
            elif url.endswith('html'):
                if url.startswith('http'):
                    continue
                assert os.path.isfile('_static/tp-caml/%s' % url.replace('ht', ''))
                with open('tp/%s' % url.replace('.html', '.rst'), 'w') as code:
                    code.write('%s' % title + '\n')
                    code.write('=' * len(title) + '\n')
                    code.write('\n.. highlight:: ocaml\n\n')
                    code.write(last_subject + '\n')
                    code.write('- `Retour à la page des TP </tp/>`_\n')
                    code.write('\n.. literalinclude:: /_static/tp-caml/%s' % url.replace('ht', ''))
