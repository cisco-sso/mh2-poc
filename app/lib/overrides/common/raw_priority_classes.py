#!/usr/bin/env python3


def raw_priority_classes(callback_values):
    data = {
        '__meta': {
            'chart': 'cisco-sso/raw',
            'version': '0.1.0'
        },
        'resources': [  # yapf: disable 
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for critical priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-critical'
                },
                'value': 100000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for high priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-high'
                },
                'value': 90000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for medium priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-medium'
                },
                'value': 80000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for low priority common pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'common-low'
                },
                'value': 70000000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for critical priority app pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-critical'
                },
                'value': 100000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for high priority app pods.',
                'globalDefault': False,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-high'
                },
                'value': 90000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for medium priority app pods.',
                'globalDefault': True,
                'kind': 'PriorityClass',
                'metadata': {
                    'name': 'app-medium'
                },
                'value': 80000
            },
            {
                'apiVersion': 'scheduling.k8s.io/v1beta1',
                'description': 'This priority class should only be used for low priority app pods.',
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
