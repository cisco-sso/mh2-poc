#!/usr/bin/env python3

# from oauth2proxy_chart import Oauth2proxyChart
from cluster_config_map import ClusterConfigMap
from base_chart import BaseChart

# 2 operations
#   override and customize


def main():
    ccm = ClusterConfigMap(fqdn="kube1.cloud.com")
    bc = BaseChart()
    bc = bc.withOverride(overrideDefaultLimits, configmap=ccm, count=2)
    bc = bc.withOverride(overrideOauth2Proxy, configmap=ccm)

    print("bc", bc)
    final = bc.generate(True)
    import pprint
    pprint.pprint(final)


def overrideDefaultLimits(values, configmap, count=1, cpu="100m", mem="64Mi"):
    values = values if values else {}
    assert configmap is not None, "configmap must be defined"

    data = {
        'priorityClassName': 'common-high',
        'replicaCount': count,
        'resources': {
            'limits': {
                'cpu': cpu,
                'memory': mem,
            },
            'requests': {
                'cpu': cpu,
                'memory': mem,
            }
        },
    }

    values.update(data)
    return values


def overrideOauth2Proxy(values, configmap):
    values = values if values else {}
    assert configmap is not None, "configmap must be defined"

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
            'clientID': 'alertmanager.{}'.format(configmap.fqdn),
            'clientSecret': '__REPLACE__',
            'configFile': '',
            'cookieSecret': '__REPLACE__'
        },
        'extraArgs': {
            'cookie-domain': 'alertmanager.{}'.format(configmap.fqdn),
            'cookie-expire': '24h',
            'cookie-secure': 'true',
            'http-address': '0.0.0.0:4180',
            'oidc-issuer-url': 'https://dex.{}'.format(configmap.fqdn),
            'provider': 'oidc',
            'redirect-url': 'https://alertmanager.{}'.format(configmap.fqdn),
            'upstream': 'http://prometheus-alertmanager'
        },
        'image': {
            'pullPolicy': 'IfNotPresent',
            'repository': 'dcwangmit01/oauth2_proxy',
            'tag': '2.2.1-alpha-20190103-debug-statements'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': 'alertmanager.{}'.format(configmap.fqdn),
                'external-dns.alpha.kubernetes.io/target': 'dyndns.kube1.cloud.com',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': ['alertmanager.{}'.format(configmap.fqdn)],
            'tls': [{
                'hosts': ['alertmanager.{}'.format(configmap.fqdn)],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'service': {
            'externalPort': 4180,
            'internalPort': 4180,
            'type': 'ClusterIP'
        }
    }

    values.update(data)
    return values


if (__name__ == '__main__'):
    main()
