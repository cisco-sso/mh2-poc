#!/usr/bin/env python3

from cluster_config_map import ClusterConfigMap
import common_overrides as co
from common_apps_chart_lib import CommonChartCollection

# chart (global), org (cisco), team (cx), project (sdp), enviroment (nonprod), cluster (sdp17), release (helm)

# namespace


# cluster = ChartCollection
class ChartCollections:
    # cluster -> enviroment=tuple(org, team, collection, namespace) -> helm_releases
    def __init__(self):
        d = {
            "common": CommonChartCollection(namespace="common"),
            #        "sdp1": SDPChartCollection(namespace="sdp1"),
            #        "sdp2": SDPChartCollection(namespace="sdp2"),
            #        "honjo1": SDPChartCollection(namespace="honjo1"),
        }
        print(d)

    def overrideCollectionOverrideChart(collection_name, release_name, **kwargs):
        # return d[collection_name].overrideChart(release_name, **kwargs)
        pass


def main():
    ccm = ClusterConfigMap(fqdn="kube1.cloud.com", namespace="common")
    gca = CommonChartCollection(ccm)  # gold standard prod
    print(gca)
    for k, v in gca.getCharts().items():
        print("#####\n", k, "\n", v.toYaml())

    print("*" * 69)
    # new chart collection with all same configs, except replica-count == 99
    gca.overrideChart("oauth2-proxy-kibana", co.set_replica_count, count=99)
    gca.overrideChart("oauth2-proxy-kibana", set_my_override, who="Josh")
    print(gca)
    for k, v in gca.getCharts().items():
        print("#####\n", k, "\n", v.toYaml())


def set_my_override(callback_values, who=None):
    data = {
        'who': who,
    }

    callback_values.update(data)
    return callback_values


if (__name__ == '__main__'):
    main()
