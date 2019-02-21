#!/usr/bin/env python3


def external_dns(callback_values):

    dict = {
        '__meta': {
            'chart': 'stable/external-dns',
            'version': '1.2.0'
        },
        'cloudflare': {
            'apiKey': '__REPLACE__',
            'email': '__REPLACE__'
        },
        'domainFilters': ['davidwang.com'],
        'logLevel': 'debug',
        'priorityClassName': 'common-medium',
        'provider': 'cloudflare',
        'rbac': {
            'apiVersion': 'v1',
            'create': True,
            'serviceAccountName': 'external-dns'
        },
        'resources': {
            'limits': {
                'cpu': '500m',
                'memory': '64Mi'
            },
            'requests': {
                'cpu': '100m',
                'memory': '64Mi'
            }
        }
    }

    callback_values.update(data)
    return callback_values
