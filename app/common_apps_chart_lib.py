#!/usr/bin/env python3

from collections import OrderedDict
from base_chart import BaseChart
import common_overrides as co


class BaseChartCollection:
    __slots__ = ['chart_dict', 'configmap']

    def __init__(self, configmap):
        self.configmap = configmap
        self.chart_dict = OrderedDict()

        self.initialize()

    def getCharts(self):
        return self.chart_dict

    def getChart(self, release_name):
        assert release_name in self.chart_dict, f"{release_name} not found in chart_dict"
        return self.chart_dict[release_name]

    def overrideChart(self, release_name, function, **kwargs):
        assert release_name in self.chart_dict, f"{release_name} not found in chart_dict"
        c = self.chart_dict[release_name]
        c = c.withOverride(function, **kwargs)
        self.chart_dict[release_name] = c
        return c


class CommonChartCollection(BaseChartCollection):
    def initialize(self):

        base = BaseChart() \
            .withO(co.set_namespace) \
            .withO(co.set_resource_limits) \
            .withO(co.set_priority_class) \
            .withO(co.set_replica_count)

        n = 'raw_priority_classes'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='incubator/raw',
                       version='0.1.0') \
                .withO(set_raw_priority_classes)
        self.chart_dict[n] = t

        n = 'raw_oauth2_proxy_accesslist_core'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='incubator/raw',
                       version='0.1.0') \
                .withO(set_raw_oauth2_proxy_accesslist,
                       email_id_list=["user1@domain.com", "user2@domain.com", "user3@domain.com"])
        self.chart_dict[n] = t

        n = 'raw_cluster_role_bindings'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='incubator/raw',
                       version='0.1.0') \
                .withO(set_raw_cluster_role_bindings)
        self.chart_dict[n] = t

        n = 'raw_limit_ranges'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='incubator/raw',
                       version='0.1.0') \
                .withO(set_raw_limit_ranges)
        self.chart_dict[n] = t

        n = 'oauth2_proxy_alertmanager'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2_proxy,
                       configmap=self.configmap,
                       hostname="alertmanager",
                       upstream_url="http://prometheus-alertmanager")
        self.chart_dict[n] = t

        n = 'oauth2_proxy_grafana'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2_proxy,
                       configmap=self.configmap,
                       hostname="grafana",
                       upstream_url="http://grafana")
        self.chart_dict[n] = t

        n = 'oauth2_proxy_kibana'
        t = base.withO(co.set_chart_meta,
                       release_name=n,
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2_proxy,
                       configmap=self.configmap,
                       hostname="kibana",
                       upstream_url="http://kibana")
        self.chart_dict[n] = t


#####################################################################
#####################################################################


def set_template(callback_values, email_id_list):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
    }

    callback_values.update(data)
    return callback_values


def set_raw_priority_classes(callback_values):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [  # yapf: disable
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for critical priority common '
                'pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-critical'
                },
                'value': 100000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for high priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-high'
                },
                'value': 90000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for medium priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-medium'
                },
                'value': 80000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for low priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-low'
                },
                'value': 70000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for critical priority app pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-critical'
                },
                'value': 100000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for high priority app pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-high'
                },
                'value': 90000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for medium priority app pods.',
                'globalDefault': True,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-medium'
                },
                'value': 80000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be '
                'used for low priority app pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-low'
                },
                'value': 70000
            }
        ]
    }
    callback_values.update(data)
    return callback_values


def set_raw_oauth2_proxy_accesslist(callback_values, email_id_list=None):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [{
            'apiVersion': 'v1',
            'data': {
                'restricted_user_access': "\n".join(email_id_list),
            },
            'kind': 'ConfigMap',
            'metadata': {
                'labels': {
                    'app': 'oauth2-proxy'
                },
                'name': 'oauth2-proxy-accesslist-core'
            }
        }]
    }

    callback_values.update(data)
    return callback_values


def set_raw_cluster_role_bindings(callback_values):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [  # yapf: disable
            {
                'apiVersion': 'rbac.authorization.k8s.io/v1',
                'kind': 'ClusterRoleBinding',
                'metadata': {
                    'name': 'oidc-cluster-admin'
                },
                'roleRef': {
                    'apiGroup': 'rbac.authorization.k8s.io',
                    'kind': 'ClusterRole',
                    'name': 'cluster-admin'
                },
                'subjects': [{
                    'apiGroup': 'rbac.authorization.k8s.io',
                    'kind': 'Group',
                    'name': 'kubernetes-admins'
                }]
            }
        ]
    }
    callback_values.update(data)
    return callback_values


def set_oauth2_proxy(callback_values,
                     configmap,
                     hostname,
                     upstream_url,
                     authenticated_emails_enabled=False,
                     authenticated_emails_template="",
                     configFile="",
                     enable_dyndns_annotation=False):
    # Checks
    assert configmap, "configmap must be defined"
    assert hostname, "hostname must be defined"
    assert upstream_url, "Upstream must be defined: 'https://upstream-service'"
    if authenticated_emails_enabled and not authenticated_emails_template:
        assert False, "authenticated_emails_template must be defined"

    host_fqdn = hostname + '.' + configmap.fqdn
    oidc_fqdn = 'dex.{}'.format(configmap.fqdn)

    data = {
        'authenticatedEmailsFile': {
            'enabled': authenticated_emails_enabled,
            'template': authenticated_emails_template,
        },
        'config': {
            'clientID': host_fqdn,
            'clientSecret': configmap.ensureSecret(host_fqdn + "-clientsecret"),
            'configFile': '{}'.format(configFile),
            'cookieSecret': configmap.ensureSecret(host_fqdn + "-cookiesecret"),
        },
        'extraArgs': {
            'cookie-domain': host_fqdn,
            'cookie-expire': '24h',
            'cookie-secure': 'true',
            'http-address': '0.0.0.0:4180',
            'oidc-issuer-url': 'https://' + oidc_fqdn,
            'provider': 'oidc',
            'redirect-url': 'https://' + host_fqdn,
            'upstream': upstream_url,
        },
        'image': {
            'pullPolicy': 'IfNotPresent',
            'repository': 'dcwangmit01/oauth2_proxy',
            'tag': 'cisco-oidc.20190103'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': host_fqdn,
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': [host_fqdn],
            'tls': [{
                'hosts': [host_fqdn],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'service': {
            'externalPort': 4180,
            'internalPort': 4180,
            'type': 'ClusterIP'
        }
    }

    if enable_dyndns_annotation:
        dyndns_annotation = 'dyndns.{}'.format(configmap.fqdn)
        data['ingress']['annotations']['external-dns.alpha.kubernetes.io/target'] = dyndns_annotation

    callback_values.update(data)
    return callback_values
