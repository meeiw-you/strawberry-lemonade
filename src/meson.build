pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'strawberry_lemonade')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
    input: 'strawberry_lemonade.in',
    output: 'strawberry_lemonade',
    configuration: conf,
    install: true,
    install_dir: get_option('bindir')
)

strawberry_lemonade_sources = [
    '__init__.py',
    'main.py',
    'test.py',
    'start.sh',
    'folder bot-env'
]

install_data(strawberry_lemonade_sources, install_dir: moduledir)
