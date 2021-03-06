import os

MAZER_HOME = os.environ.get('MAZER_HOME', None) or '~/.ansible'
DEFAULT_CONFIG_FILE = '~/.ansible/mazer.yml'


def get_config_path():
    paths = [
        'mazer.yml',
        os.path.join(MAZER_HOME, 'mazer.yml'),
        '/etc/ansible/mazer.yml'
    ]
    for path in paths:
        if os.path.exists(os.path.expanduser(path)):
            return path
    return paths[1]


# a list of tuples that is fed to an OrderedDict
DEFAULTS = [
    ('server',
     {'url': 'https://galaxy.ansible.com',
      'ignore_certs': False}
     ),

    # In order of priority
    ('content_path', os.path.join(MAZER_HOME, 'collections/ansible_collections')),
    ('global_content_path', '/usr/share/ansible/collections/ansible_collections'),

    # runtime options
    ('options',
     {
         # TODO: no other options, rm 'options'
     }

     ),
    ('version', 1),
]

# FIXME: replace with logging config
VERBOSITY = 0
CONFIG_FILE = get_config_path()
