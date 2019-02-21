#!/usr/bin/env python3


def set_chart_meta(callback_values, release_name, chart=None, version=None, namespace='default'):
    # chart and version are optional if they are already defined, otherwise required
    if chart is None:
        assert chart in callback_values['__meta'], "Chart must be defined"
    if version is None:
        assert version in callback_values['__meta'], "Version must be defined"

    data = {
        '__meta': {
            'release_name': release_name,
            'chart': chart,
            'version': version,
            'namespace': namespace,
        },
    }

    callback_values.update(data)
    return callback_values


def set_namespace(callback_values, namespace="default"):
    data = {
        'namespace': namespace,
    }

    callback_values.update(data)
    return callback_values


def set_replica_count(callback_values, count=1):
    data = {
        'replicaCount': count,
    }

    callback_values.update(data)
    return callback_values


def set_priority_class(callback_values, name="common-low"):
    data = {
        'priorityClassName': 'common-high',
    }

    callback_values.update(data)
    return callback_values


def set_resource_limits(callback_values, cpu_limit="100m", mem_limit="64Mi", cpu_request="100m", mem_request="64Mi"):
    data = {
        'resources': {
            'limits': {
                'cpu': cpu_limit,
                'memory': mem_limit,
            },
            'requests': {
                'cpu': cpu_request,
                'memory': mem_request,
            },
        },
    }

    callback_values.update(data)
    return callback_values
