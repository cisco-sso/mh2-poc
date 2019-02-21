#!/usr/bin/env python3


def xxx(callback_values):

    dict = {
        '__meta': {
            'chart': 'cisco-sso/gangway',
            'version': '0.1.0'
        },
        'affinity': {
            'podAntiAffinity': {
                'preferredDuringSchedulingIgnoredDuringExecution': [{
                    'podAffinityTerm': {
                        'labelSelector': {
                            'matchLabels': {
                                'release': 'gangway'
                            }
                        },
                        'topologyKey': 'failure-domain.beta.kubernetes.io/zone'
                    },
                    'weight': 50
                }],
                'requiredDuringSchedulingIgnoredDuringExecution': [{
                    'labelSelector': {
                        'matchLabels': {
                            'release': 'gangway'
                        }
                    },
                    'topologyKey': 'kubernetes.io/hostname',
                    'weight': 40
                }]
            }
        },
        'configFiles': {
            'gangway.yaml':
            '\n'
            '## The address to listen on. Defaults '
            'to 0.0.0.0 to listen on all '
            'interfaces.\n'
            'host: 0.0.0.0\n'
            '\n'
            '## The port to listen on. Defaults to '
            '8080.\n'
            'port: 8080\n'
            '\n'
            '## Should Gangway serve TLS vs. plain '
            'HTTP? Default: false\n'
            'serveTLS: false\n'
            '\n'
            '## The public cert file (including '
            'root and intermediates) to use when '
            'serving TLS.\n'
            'certFile: "/etc/gangway/tls/tls.crt"\n'
            '\n'
            '## The private key file when serving '
            'TLS.\n'
            'keyFile: "/etc/gangway/tls/tls.key"\n'
            '\n'
            '## The cluster name. Used in UI and '
            'kubectl config instructions.\n'
            'clusterName: '
            '"__REPLACE_CLUSTER_FQDN__"\n'
            '\n'
            '## OAuth2 URL to start authorization '
            'flow.\n'
            'authorizeURL: '
            '"https://dex.__REPLACE_CLUSTER_FQDN__/auth"\n'
            '\n'
            '## OAuth2 URL to obtain access '
            'tokens.\n'
            'tokenURL: '
            '"https://dex.__REPLACE_CLUSTER_FQDN__/token"\n'
            '\n'
            '## Endpoint that provides user profile '
            'information [optional]. Not all '
            'providers will require this.\n'
            '#audience: '
            '"https://dex.__REPLACE_CLUSTER_FQDN__/userinfo"\n'
            '\n'
            '## Where to redirect back to. This '
            'should be a URL where gangway is '
            'reachable. Typically this also needs '
            'to be\n'
            '## registered as part of the oauth '
            'application with the oAuth provider.\n'
            'redirectURL: '
            '"https://gangway.__REPLACE_CLUSTER_FQDN__/callback"\n'
            '\n'
            '## API client ID as indicated by the '
            'identity provider.\n'
            'clientID: '
            '"gangway.__REPLACE_CLUSTER_FQDN__"\n'
            "clientSecret: '__REPLACE__'\n"
            "sessionSecurityKey: '__REPLACE__'\n"
            '\n'
            '## The JWT claim to use as the '
            'username. This is used in UI.\n'
            'usernameClaim: "email"\n'
            '\n'
            '## The JWT claim to use as the email '
            'claim. This is used to name the "user" '
            'part of the config.\n'
            'emailClaim: "email"\n'
            '\n'
            '## The API server endpoint used to '
            'configure kubectl.\n'
            'apiServerURL: '
            '"https://api.__REPLACE_CLUSTER_FQDN__:6443"\n'
            '\n'
            '## The path to find the CA bundle for '
            'the API server. Used to configure '
            'kubectl. This is typically mounted '
            'into the\n'
            '## default location for workloads '
            'running on a Kubernetes cluster and '
            "doesn't need to be set.\n"
            'clusterCAPath: '
            '"/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"\n'
            '\n'
            '## Used to specify the scope of the '
            'requested OAuth authorization.\n'
            'scopes: ["openid", "profile", "email", '
            '"offline_access", "groups"]'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/target': 'dyndns.davidwang.com',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': ['gangway.__REPLACE_CLUSTER_FQDN__'],
            'path': '/',
            'tls': [{
                'hosts': ['gangway.__REPLACE_CLUSTER_FQDN__'],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'priorityClassName': 'common-high',
        'replicaCount': 1,
        'resources': {
            'limits': {
                'cpu': '100m',
                'memory': '128Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '128Mi'
            }
        },
        'secrets': []
    }

    callback_values.update(data)
    return callback_values
