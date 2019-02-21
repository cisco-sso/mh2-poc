#!/usr/bin/env python3


def gangway(callback_values):
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
            'gangway.yaml': _gangway_yaml()
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


def _gangway_yaml():
    str = """
## The address to listen on. Defaults to 0.0.0.0 to listen on all interfaces.
host: 0.0.0.0

## The port to listen on. Defaults to 8080.
port: 8080

## Should Gangway serve TLS vs. plain HTTP? Default: false
serveTLS: false

## The public cert file (including root and intermediates) to use when serving TLS.
certFile: "/etc/gangway/tls/tls.crt"

## The private key file when serving TLS.
keyFile: "/etc/gangway/tls/tls.key"

## The cluster name. Used in UI and kubectl config instructions.
clusterName: "__REPLACE_CLUSTER_FQDN__"

## OAuth2 URL to start authorization flow.
authorizeURL: "https://dex.__REPLACE_CLUSTER_FQDN__/auth"

## OAuth2 URL to obtain access tokens.
tokenURL: "https://dex.__REPLACE_CLUSTER_FQDN__/token"

## Endpoint that provides user profile information [optional]. Not all providers will require this.
#audience: "https://dex.__REPLACE_CLUSTER_FQDN__/userinfo"

## Where to redirect back to. This should be a URL where gangway is reachable. Typically this also needs to be
## registered as part of the oauth application with the oAuth provider.
redirectURL: "https://gangway.__REPLACE_CLUSTER_FQDN__/callback"

## API client ID as indicated by the identity provider.
clientID: "gangway.__REPLACE_CLUSTER_FQDN__"
clientSecret: '__REPLACE__'
sessionSecurityKey: '__REPLACE__'

## The JWT claim to use as the username. This is used in UI.
usernameClaim: "email"

## The JWT claim to use as the email claim. This is used to name the "user" part of the config.
emailClaim: "email"

## The API server endpoint used to configure kubectl.
apiServerURL: "https://api.__REPLACE_CLUSTER_FQDN__:6443"

## The path to find the CA bundle for the API server. Used to configure kubectl. This is typically mounted into the
## default location for workloads running on a Kubernetes cluster and doesn't need to be set.
clusterCAPath: "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"

## Used to specify the scope of the requested OAuth authorization.
scopes: ["openid", "profile", "email", "offline_access", "groups"]
"""
    return str
