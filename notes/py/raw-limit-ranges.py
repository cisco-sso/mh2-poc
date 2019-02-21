{   '__meta': {'chart': 'cisco-sso/raw', 'version': '0.1.0'},
    'resources': [   {   'apiVersion': 'v1',
                         'kind': 'LimitRange',
                         'metadata': {'name': 'limits'},
                         'spec': {   'limits': [   {   'default': {   'cpu': '100m',
                                                                      'memory': '256Mi'},
                                                       'defaultRequest': {   'cpu': '100m',
                                                                             'memory': '256Mi'},
                                                       'type': 'Container'}]}}]}
