#!/usr/bin/env python3


def xxx(callback_values):

    dict = {
        '__meta': {
            'chart': 'incubator/elasticsearch',
            'version': '1.4.0'
        },
        'appVersion': '6.3.1',
        'client': {
            'antiAffinity': 'hard',
            'heapSize': '2048m',
            'priorityClassName': 'common-critical',
            'replicas': 1,
            'resources': {
                'limits': {
                    'cpu': 1,
                    'memory': '2560Mi'
                },
                'requests': {
                    'cpu': '100m',
                    'memory': '2560Mi'
                }
            }
        },
        'cluster': {
            'env': {
                'NETWORK_HOST': '_eth0:ipv4_'
            }
        },
        'data': {
            'antiAffinity': 'hard',
            'heapSize': '3072m',
            'persistence': {
                'size': '16Gi'
            },
            'priorityClassName': 'common-critical',
            'replicas': 1,
            'resources': {
                'limits': {
                    'cpu': 1,
                    'memory': '3840Mi'
                },
                'requests': {
                    'cpu': '100m',
                    'memory': '3840Mi'
                }
            }
        },
        'image': {
            'tag': '6.3.1'
        },
        'master': {
            'antiAffinity': 'soft',
            'heapSize': '1024m',
            'persistence': {
                'size': '1Gi'
            },
            'priorityClassName': 'common-critical',
            'replicas': 2,
            'resources': {
                'limits': {
                    'cpu': 1,
                    'memory': '1536Mi'
                },
                'requests': {
                    'cpu': '100m',
                    'memory': '1536Mi'
                }
            }
        }
    }

    callback_values.update(data)
    return callback_values
