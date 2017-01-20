import os, jinja2

posters = [file.replace('.jpg', '') for file in os.listdir('_static/demotivators') if file[0] != '.']
template = jinja2.Template(open('_templates/demotivator.rst').read())
open('demotivators/index.rst', 'w').write(template.render({'posters': posters}))
for poster in posters:
    directory = os.path.join('demotivators', poster)
    if not os.path.exists(directory):
        os.makedirs(directory)
    open('demotivators/{}/index.rst'.format(poster), 'w').write(template.render({'posters': posters, 'poster': poster}))
