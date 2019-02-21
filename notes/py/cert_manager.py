#!/usr/bin/env python3


def cert_manager(callback_values):
    data = {
        '__meta': {
            'chart': 'stable/cert-manager',
            'version': 'v0.5.2'
        },
        'ingressShim': {
            'enabled': False
        },
        'rbac': {
            'create': True
        },
        'resources': {
            'limits': {
                'cpu': '100m',
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
