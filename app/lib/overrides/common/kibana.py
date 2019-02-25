#!/usr/bin/env python3


def kibana(callback_values):
    data = {
        '__meta': {
            'chart': 'stable/kibana',
            'version': '0.8.0'
        },
        'affinity': {
            'podAntiAffinity': {
                'preferredDuringSchedulingIgnoredDuringExecution': [{
                    'podAffinityTerm': {
                        'labelSelector': {
                            'matchLabels': {
                                'release': 'kibana'
                            }
                        },
                        'topologyKey': 'failure-domain.beta.kubernetes.io/zone'
                    },
                    'weight': 50
                }],
                'requiredDuringSchedulingIgnoredDuringExecution': [{
                    'labelSelector': {
                        'matchLabels': {
                            'release': 'kibana'
                        }
                    },
                    'topologyKey': 'kubernetes.io/hostname',
                    'weight': 40
                }]
            }
        },
        'env': {
            'ELASTICSEARCH_URL': 'http://elasticsearch-client:9200',
            'LOGGING_VERBOSE': 'false',
            'SERVER_DEFAULTROUTE': '/app/kibana',
            'SERVER_PORT': 5601
        },
        'image': {
            'repository': 'docker.elastic.co/kibana/kibana-oss',
            'tag': '6.3.1'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': 'kibana.__REPLACE_CLUSTER_FQDN__',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/auth-realm': 'Authentication Required',
                'nginx.ingress.kubernetes.io/auth-secret': 'common-basic-auth',
                'nginx.ingress.kubernetes.io/auth-type': 'basic',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': False,
            'hosts': ['kibana.__REPLACE_CLUSTER_FQDN__'],
            'tls': [{
                'hosts': ['kibana.__REPLACE_CLUSTER_FQDN__'],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'priorityClassName': 'common-critical',
        'replicaCount': 1,
        'resources': {
            'limits': {
                'cpu': 1,
                'memory': '256Mi'
            },
            'requests': {
                'cpu': '200m',
                'memory': '256Mi'
            }
        },
        'service': {
            'externalPort': 5601,
            'internalPort': 5601,
            'type': 'ClusterIP'
        }
    }

    callback_values.update(data)
    return callback_values
