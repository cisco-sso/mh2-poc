#!/usr/bin/env python3


def dex(callback_values):
    data = {
        '__meta': {
            'chart': 'stable/dex',
            'version': '0.5.0'
        },
        'config': {
            'connectors': [{
                'config': {
                    'clientID': '__REPLACE__',
                    'clientSecret': '__REPLACE__',
                    'org': '__REPLACE__',
                    'redirectURI': 'https://dex.__REPLACE_CLUSTER_FQDN__/callback'
                },
                'id': 'github',
                'name': 'GitHub',
                'type': 'github'
            }],
            'enablePasswordDB':
            False,
            'issuer':
            'https://dex.__REPLACE_CLUSTER_FQDN__/',
            'oauth2': {
                'responseTypes': ['code', 'token', 'id_token'],
                'skipApprovalScreen': True
            },
            'staticClients': [  # yapf: disable
                {
                    'id': 'alertmanager.__REPLACE_CLUSTER_FQDN__',
                    'name': 'alertmanager',
                    'redirectURIs': ['https://alertmanager.__REPLACE_CLUSTER_FQDN__/oauth2/callback'],
                    'secret': '__REPLACE__'
                },
                {
                    'id': 'gangway.__REPLACE_CLUSTER_FQDN__',
                    'name': 'gangway',
                    'redirectURIs': ['https://gangway.__REPLACE_CLUSTER_FQDN__/callback'],
                    'secret': '__REPLACE__'
                },
                {
                    'id': 'grafana.__REPLACE_CLUSTER_FQDN__',
                    'name': 'grafana',
                    'redirectURIs': ['https://grafana.__REPLACE_CLUSTER_FQDN__/oauth2/callback'],
                    'secret': '__REPLACE__'
                },
                {
                    'id': 'kibana.__REPLACE_CLUSTER_FQDN__',
                    'name': 'kibana',
                    'redirectURIs': ['https://kibana.__REPLACE_CLUSTER_FQDN__/oauth2/callback'],
                    'secret': '__REPLACE__'
                },
                {
                    'id': 'prometheus.__REPLACE_CLUSTER_FQDN__',
                    'name': 'prometheus',
                    'redirectURIs': ['https://prometheus.__REPLACE_CLUSTER_FQDN__/oauth2/callback'],
                    'secret': '__REPLACE__'
                },
                {
                    'id': 'oidcdebugger.com',
                    'name': 'oidcdebugger',
                    'redirectURIs': ['https://oidcdebugger.com/debug'],
                    'secret': '__REPLACE__'
                }
            ],
            'storage': {
                'config': {
                    'inCluster': True
                },
                'type': 'kubernetes'
            },
            'web': {
                'http': '0.0.0.0:8080'
            }
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/target': 'dyndns.davidwang.com',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': ['dex.__REPLACE_CLUSTER_FQDN__'],
            'path': '/',
            'tls': [{
                'hosts': ['dex.__REPLACE_CLUSTER_FQDN__'],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'ports': [{
            'containerPort': 8080,
            'name': 'http',
            'protocol': 'TCP'
        }, {
            'containerPort': 5000,
            'name': 'grpc',
            'protocol': 'TCP'
        }],
        'rbac': {
            'create': True
        },
        'replicas':
        1,
        'resources': {
            'limits': {
                'cpu': '100m',
                'memory': '50Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '50Mi'
            }
        },
        'serviceAccount': {
            'create': True
        }
    }

    callback_values.update(data)
    return callback_values
