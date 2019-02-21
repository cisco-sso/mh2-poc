{
    '__meta': {
        'chart': 'stable/oauth2-proxy',
        'version': '0.6.0'
    },
    'authenticatedEmailsFile': {
        'enabled': True,
        'template': 'oauth2-proxy-accesslist-core'
    },
    'config': {
        'clientID': 'alertmanager.__REPLACE_CLUSTER_FQDN__',
        'clientSecret': '__REPLACE__',
        'configFile': '',
        'cookieSecret': '__REPLACE__'
    },
    'extraArgs': {
        'cookie-domain': 'alertmanager.__REPLACE_CLUSTER_FQDN__',
        'cookie-expire': '24h',
        'cookie-secure': 'true',
        'http-address': '0.0.0.0:4180',
        'oidc-issuer-url': 'https://dex.__REPLACE_CLUSTER_FQDN__/',
        'provider': 'oidc',
        'redirect-url': 'https://alertmanager.__REPLACE_CLUSTER_FQDN__',
        'upstream': 'http://prometheus-alertmanager'
    },
    'image': {
        'pullPolicy': 'IfNotPresent',
        'repository': 'dcwangmit01/oauth2_proxy',
        'tag': '2.2.1-alpha-20190103-debug-statements'
    },
    'ingress': {
        'annotations': {
            'external-dns.alpha.kubernetes.io/hostname': 'alertmanager.__REPLACE_CLUSTER_FQDN__',
            'external-dns.alpha.kubernetes.io/target': 'dyndns.davidwang.com',
            'kubernetes.io/ingress.class': 'nginx',
            'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
        },
        'enabled': True,
        'hosts': ['alertmanager.__REPLACE_CLUSTER_FQDN__'],
        'tls': [{
            'hosts': ['alertmanager.__REPLACE_CLUSTER_FQDN__'],
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
