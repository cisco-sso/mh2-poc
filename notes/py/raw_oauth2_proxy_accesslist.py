#!/usr/bin/env python3


def raw_oauth2_proxy_accesslist(callback_values):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [{
            'apiVersion': 'v1',
            'data': {
                'restricted_user_access': 'dcwangmit01@gmail.com\n'
                'jmdots@gmail.com\n'
                'rluckie@gmail.com'
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
