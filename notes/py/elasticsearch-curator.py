{   '__meta': {'chart': 'incubator/elasticsearch-curator', 'version': '0.4.0'},
    'config': {   'elasticsearch': {   'hosts': ['elasticsearch-client'],
                                       'master_only': False,
                                       'timeout': 30,
                                       'use_ssl': False}},
    'configMaps': {   'action_file_yml': 'actions:\n'
                                         '  0:\n'
                                         '    action: delete_indices\n'
                                         '    description: Clean up old '
                                         'indices but skip the .kibana index\n'
                                         '    options:\n'
                                         '      ignore_empty_list: True\n'
                                         '    filters:\n'
                                         '      - filtertype: kibana\n'
                                         '        exclude: True\n'
                                         '      - filtertype: age\n'
                                         '        source: name\n'
                                         '        direction: older\n'
                                         "        timestring: '%Y.%m.%d'\n"
                                         '        unit: days\n'
                                         '        unit_count: 7'},
    'cronjob': {'concurrencyPolicy': 'Replace', 'schedule': '0 * * * *'},
    'priorityClassName': 'common-high'}
