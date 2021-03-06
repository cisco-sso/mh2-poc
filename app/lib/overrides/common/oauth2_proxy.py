#!/usr/bin/env python3


def oauth2_proxy(callback_values):
    data = {
        '__meta': {
            'chart': 'stable/oauth2-proxy',
            'version': '0.6.0'
        },
        'authenticatedEmailsFile': {
            'enabled': True,
            'template': 'oauth2-proxy-accesslist-core'
        },
        'config': {
            'clientID': 'grafana.__REPLACE_CLUSTER_FQDN__',
            'clientSecret': '__REPLACE__',
            'configFile': '',
            'cookieSecret': '__REPLACE__'
        },
        'extraArgs': {
            'cookie-domain': 'grafana.__REPLACE_CLUSTER_FQDN__',
            'cookie-expire': '24h',
            'cookie-secure': 'true',
            'http-address': '0.0.0.0:4180',
            'oidc-issuer-url': 'https://dex.__REPLACE_CLUSTER_FQDN__/',
            'provider': 'oidc',
            'redirect-url': 'https://grafana.__REPLACE_CLUSTER_FQDN__',
            'upstream': 'http://grafana'
        },
        'image': {
            'pullPolicy': 'IfNotPresent',
            'repository': 'dcwangmit01/oauth2_proxy',
            'tag': '2.2.1-alpha-20190103-debug-statements'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': 'grafana.__REPLACE_CLUSTER_FQDN__',
                'external-dns.alpha.kubernetes.io/target': 'dyndns.davidwang.com',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': ['grafana.__REPLACE_CLUSTER_FQDN__'],
            'tls': [{
                'hosts': ['grafana.__REPLACE_CLUSTER_FQDN__'],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'priorityClassName': 'common-high',
        'replicaCount': 1,
        'resources': {
            'limits': {
                'cpu': '100m',
                'memory': '64Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '64Mi'
            }
        },
        'service': {
            'externalPort': 4180,
            'internalPort': 4180,
            'type': 'ClusterIP'
        }
    }

    callback_values.update(data)
    return callback_values
