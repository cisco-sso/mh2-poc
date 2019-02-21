#!/usr/bin/env python3


def grafana(callback_values):
    dict = {
        '__meta': {
            'chart': 'stable/grafana',
            'version': '1.13.1'
        },
        'adminUser': 'admin',
        'dashboardProviders': {
            'dashboardproviders.yaml': {
                'apiVersion':
                1,
                'providers': [{
                    'disableDeletion': False,
                    'editable': True,
                    'folder': '',
                    'name': 'default',
                    'options': {
                        'path': '/var/lib/grafana/dashboards/default'
                    },
                    'orgId': 1,
                    'type': 'file'
                }]
            }
        },
        'dashboards': {
            'default': {
                'elasticsearch-infinity': {
                    'datasource': 'Prometheus',
                    'gnetId': 6483,
                    'revision': 1
                },
                'kubernetes-capacity': {
                    'datasource': 'Prometheus',
                    'gnetId': 5309
                },
                'kubernetes-cluster-health': {
                    'datasource': 'Prometheus',
                    'gnetId': 5312
                },
                'kubernetes-cluster-monitoring-via-prometheus': {
                    'datasource': 'Prometheus',
                    'gnetId': 1621
                },
                'kubernetes-cluster-status': {
                    'datasource': 'Prometheus',
                    'gnetId': 5315
                },
                'kubernetes-deployment': {
                    'datasource': 'Prometheus',
                    'gnetId': 5303
                },
                'kubernetes-master-status': {
                    'datasource': 'Prometheus',
                    'gnetId': 5318
                },
                'kubernetes-node-exporter-full': {
                    'datasource': 'Prometheus',
                    'gnetId': 3320
                },
                'kubernetes-nodes': {
                    'datasource': 'Prometheus',
                    'gnetId': 5324
                },
                'kubernetes-pods': {
                    'datasource': 'Prometheus',
                    'gnetId': 5327
                },
                'kubernetes-resource-requests': {
                    'datasource': 'Prometheus',
                    'gnetId': 5321
                },
                'kubernetes-statefulsets': {
                    'datasource': 'Prometheus',
                    'gnetId': 5330
                },
                'node-exporter-service-metrics': {
                    'datasource': 'Prometheus',
                    'gnetId': 405,
                    'revision': 6
                },
                'prometheus-stats': {
                    'datasource': 'Prometheus',
                    'gnetId': 2,
                    'revision': 2
                }
            }
        },
        'datasources': {
            'datasources.yaml': {
                'apiVersion':
                1,
                'datasources': [{
                    'access': 'proxy',
                    'isDefault': True,
                    'name': 'Prometheus',
                    'type': 'prometheus',
                    'url': 'http://prometheus-server'
                }]
            }
        },
        'grafana.ini': {
            'auth.basic': {
                'enabled': False
            },
            'auth.proxy': {
                'enabled': True,
                'header_name': 'X-Forwarded-User'
            },
            'log': {
                'mode': 'console'
            },
            'paths': {
                'data': '/var/lib/grafana/data',
                'logs': '/var/log/grafana',
                'plugins': '/var/lib/grafana/plugins'
            },
            'users': {
                'auto_assign_org_role': 'Admin'
            }
        },
        'image': {
            'tag': '5.2.2'
        },
        'ingress': {
            'annotations': {
                'external-dns.alpha.kubernetes.io/hostname': 'grafana.__REPLACE_CLUSTER_FQDN__',
                'kubernetes.io/ingress.class': 'nginx',
                'nginx.ingress.kubernetes.io/auth-realm': 'Authentication '
                'Required',
                'nginx.ingress.kubernetes.io/auth-secret': 'common-basic-auth',
                'nginx.ingress.kubernetes.io/auth-type': 'basic',
                'nginx.ingress.kubernetes.io/force-ssl-redirect': 'true'
            },
            'enabled': False,
            'hosts': ['grafana.__REPLACE_CLUSTER_FQDN__'],
            'tls': [{
                'hosts': ['grafana.__REPLACE_CLUSTER_FQDN__'],
                'secretName': 'wildcard-production-tls'
            }]
        },
        'persistence': {
            'accessModes': ['ReadWriteOnce'],
            'enabled': True,
            'size': '1Gi'
        },
        'plugins': None,
        'rbac': {
            'enable': True
        },
        'replicas': 1,
        'resources': {
            'limits': {
                'cpu': '100m',
                'memory': '100Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '100Mi'
            }
        },
        'serviceAccount': {
            'create': True
        }
    }

    callback_values.update(data)
    return callback_values
