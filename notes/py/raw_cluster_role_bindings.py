#!/usr/bin/env python3


def xxx(callback_values):

    dict = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [{
            'apiVersion':
            'rbac.authorization.k8s.io/v1',
            'kind':
            'ClusterRoleBinding',
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
        }]
    }

    callback_values.update(data)
    return callback_values
