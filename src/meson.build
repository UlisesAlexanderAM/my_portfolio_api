pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'job_hunting_helper')
gnome = import('gnome')

gnome.compile_resources('job_hunting_helper',
  'job_hunting_helper.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'job_hunting_helper.in',
  output: 'job_hunting_helper',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

job_hunting_helper_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(job_hunting_helper_sources, install_dir: moduledir)
