#!/usr/bin/env python3


def elasticsearch_curator(callback_values):

    data = {
        '__meta': {
            'chart': 'incubator/elasticsearch-curator',
            'version': '0.4.0'
        },
        'config': {
            'elasticsearch': {
                'hosts': ['elasticsearch-client'],
                'master_only': False,
                'timeout': 30,
                'use_ssl': False
            }
        },
        'configMaps': {
            'action_file_yml': _action_file()
        },
        'cronjob': {
            'concurrencyPolicy': 'Replace',
            'schedule': '0 * * * *'
        },
        'priorityClassName': 'common-high'
    }

    callback_values.update(data)
    return callback_values


def _action_file():
    str = """
actions:
  0:
    action: delete_indices
    description: Clean up old indices but skip the .kibana index
    options:
      ignore_empty_list: True
    filters:
      - filtertype: kibana
        exclude: True
      - filtertype: age
        source: name
        direction: older
        timestring: '%Y.%m.%d'
        unit: days
        unit_count: 7
"""
    return str
