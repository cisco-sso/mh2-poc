#!/usr/bin/env python3

from collections import OrderedDict
from base_chart import BaseChart
import common_overrides as co


class BaseChartCollection:
    __slots__ = ['releases']

    def __init__(self):
        pass


class CommonChartCollection:
    __slots__ = ['chart_dict', 'configmap']

    def __init__(self, configmap):
        self.configmap = configmap
        self.chart_dict = OrderedDict()

        self.initialize()

    def initialize(self):

        base = BaseChart() \
            .withO(co.set_namespace) \
            .withO(co.set_resource_limits) \
            .withO(co.set_priority_class) \
            .withO(co.set_replica_count)

        # raw priority classes
        t = base.withO(co.set_chart_meta,
                       release_name='raw-priority-classes',
                       chart='incubator/raw',
                       version='0.1.0') \
                .withO(set_rawpriorityclasses)

        self.chart_dict['raw-priority-classes'] = t

        # oauth2-proxy-alertmanager
        t = base.withO(co.set_chart_meta,
                       release_name='oauth2-proxy-alertmanager',
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2proxy,
                       configmap=self.configmap,
                       hostname="alertmanager",
                       upstream_url="http://prometheus-alertmanager")
        self.chart_dict['oauth2-proxy-alertmanager'] = t

        # oauth2-proxy-grafana
        t = base.withO(co.set_chart_meta,
                       release_name='oauth2-proxy-grafana',
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2proxy,
                       configmap=self.configmap,
                       hostname="grafana",
                       upstream_url="http://grafana")
        self.chart_dict['oauth2-proxy-grafana'] = t

        # oauth2-proxy-kibana
        t = base.withO(co.set_chart_meta,
                       release_name='oauth2-proxy-kibana',
                       chart='stable/oauth2-proxy',
                       version='0.6.0') \
                .withO(set_oauth2proxy,
                       configmap=self.configmap,
                       hostname="kibana",
                       upstream_url="http://kibana")
        self.chart_dict['oauth2-proxy-kibana'] = t

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


#####################################################################
#####################################################################


def set_rawpriorityclasses(callback_values):

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


def set_oauth2proxy(callback_values,
                    configmap,
                    hostname=None,
                    upstream_url=None,
                    authenticated_emails_enabled=False,
                    authenticated_emails_template="",
                    configFile="",
                    enable_dyndns_annotation=False):
    # Checks
    assert configmap, "configmap must be defined"
    assert upstream_url, "Upstream must be defined: 'https://upstream-service'"
    if authenticated_emails_enabled and not authenticated_emails_template:
        assert False, "authenticated_emails_template must be defined"

    service_fqdn = hostname + '.' + configmap.fqdn
    oidc_fqdn = 'dex.{}'.format(configmap.fqdn)

    data = {
        'authenticatedEmailsFile': {
            'enabled': authenticated_emails_enabled,
            'template': authenticated_emails_template,
        },
        'config': {
            'clientID': service_fqdn,
            'clientSecret': configmap.ensureSecret(service_fqdn + "-client_secret"),
            'configFile': '{}'.format(configFile),
            'cookieSecret': configmap.ensureSecret(service_fqdn + "-cookie_secret"),
        },
        'extraArgs': {
            'cookie-domain': service_fqdn,
            'cookie-expire': '24h',
            'cookie-secure': 'true',
            'http-address': '0.0.0.0:4180',
            'oidc-issuer-url': 'https://' + oidc_fqdn,
            'provider': 'oidc',
            'redirect-url': 'https://' + service_fqdn,
            'upstream': upstream_url,
        },
        'image': {
            'pullPolicy': 'IfNotPresent',
            'repository': 'dcwangmit01/oauth2_proxy',
            'tag': '2.2.1-alpha-20190103-debug-statements'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': service_fqdn,
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': True,
            'hosts': [service_fqdn],
            'tls': [{
                'hosts': [service_fqdn],
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
