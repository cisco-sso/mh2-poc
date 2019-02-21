#!/usr/bin/env python3


def xxx(callback_values):

    dict = {
        '__meta': {
            'chart': 'stable/filebeat',
            'version': '1.0.5'
        },
        'config': {
            'filebeat.config': {
                'modules': {
                    'path': '${path.config}/modules.d/*.yml',
                    'reload.enabled': False
                },
                'prospectors': {
                    'path': '${path.config}/prospectors.d/*.yml',
                    'reload.enabled': False
                }
            },
            'filebeat.prospectors': [{
                'enabled': True,
                'exclude_files': ['kube\\-apiserver\\-audit\\.log$'],
                'ignore_older': '168h',
                'paths': ['/var/log/*.log', '/var/log/messages', '/var/log/syslog'],
                'type': 'log'
            },
                                     {
                                         'enabled': True,
                                         'ignore_older': '168h',
                                         'json.add_error_key': True,
                                         'paths': ['/var/log/kube-apiserver-audit.log'],
                                         'type': 'log'
                                     },
                                     {
                                         'containers.ids': ['*'],
                                         'ignore_older':
                                         '168h',
                                         'processors': [{
                                             'add_kubernetes_metadata': {
                                                 'in_cluster': True
                                             }
                                         },
                                                        {
                                                            'drop_event': {
                                                                'when': {
                                                                    'equals': {
                                                                        'kubernetes.container.name': 'filebeat'
                                                                    }
                                                                }
                                                            }
                                                        }],
                                         'type':
                                         'docker'
                                     }],
            'output.elasticsearch': {
                'hosts': ['http://elasticsearch-client:9200']
            },
            'output.file': {
                'enabled': False
            },
            'processors': [{
                'add_cloud_metadata': None
            }],
            'setup.kibana': {
                'host': 'kibana:5601'
            }
        },
        'priorityClassName': 'common-critical',
        'rbac': {
            'create': True
        },
        'resources': {
            'limits': {
                'cpu': '100m',
                'memory': '200Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '200Mi'
            }
        },
        'serviceAccount': {
            'create': True,
            'name': 'filebeat'
        },
        'tolerations': [{
            'operator': 'Exists'
        }],
        'version': '1.0.5'
    }

    callback_values.update(data)
    return callback_values
