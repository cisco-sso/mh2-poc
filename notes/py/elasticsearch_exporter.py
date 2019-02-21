#!/usr/bin/env python3


def xxx(callback_values):

    dict = {
        '__meta': {
            'chart': 'stable/elasticsearch-exporter',
            'version': '0.2.0'
        },
        'es': {
            'uri': 'http://elasticsearch-client:9200'
        },
        'priorityClassName': 'common-critical',
        'resources': {
            'limits': {
                'cpu': '500m',
                'memory': '64Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '64Mi'
            }
        },
        'service': {
            'annotations': {
                'prometheus.io/port': '9108',
                'prometheus.io/scrape': 'true'
            }
        },
        'version': '0.2.0'
    }

    callback_values.update(data)
    return callback_values
