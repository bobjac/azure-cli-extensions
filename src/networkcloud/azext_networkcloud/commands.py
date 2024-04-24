# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code originally generated by aaz-dev-tools and facilitates integration of custom code
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines,import-outside-toplevel
# pylint: disable=too-many-statements

""" Load Command model table importing custom commands"""

from ._format import (
    transform_child_resource_table_output,
    transform_cluster_manager_table_output,
    transform_hydrated_resource_table_output,
    transform_rack_sku_table_output,
    transform_resource_table_output,
)


def load_command_table(self, _):  # pylint: disable=unused-argument
    """Custom code imported in this function is loaded via:
    cli-ext/*/ext/src/networkcloud/azext_networkcloud/__init__.py
    """

    # baremetalmachine
    with self.command_group("networkcloud baremetalmachine"):
        from .aaz.latest.networkcloud.baremetalmachine import List, Show

        self.command_table["networkcloud baremetalmachine show"] = Show(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )
        self.command_table["networkcloud baremetalmachine list"] = List(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )

        from .operations.baremetalmachine._run_command import RunCommand
        from .operations.baremetalmachine._run_data_extract import RunDataExtract
        from .operations.baremetalmachine._run_read_command import RunReadCommand

        self.command_table["networkcloud baremetalmachine run-command"] = RunCommand(
            loader=self
        )
        self.command_table[
            "networkcloud baremetalmachine run-read-command"
        ] = RunReadCommand(loader=self)
        self.command_table[
            "networkcloud baremetalmachine run-data-extract"
        ] = RunDataExtract(loader=self)

    # cloudservicesnetwork
    with self.command_group("networkcloud cloudservicesnetwork"):
        from .aaz.latest.networkcloud.cloudservicesnetwork import List, Show

        self.command_table["networkcloud cloudservicesnetwork show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud cloudservicesnetwork list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

    # cluster
    with self.command_group("networkcloud cluster"):
        from .aaz.latest.networkcloud.cluster import List, Show

        self.command_table["networkcloud cluster show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud cluster list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

    # cluster baremetalmachinekeyset
    with self.command_group("networkcloud cluster baremetalmachinekeyset"):
        from .aaz.latest.networkcloud.cluster.baremetalmachinekeyset import List, Show

        self.command_table["networkcloud cluster baremetalmachinekeyset show"] = Show(
            loader=self, table_transformer=transform_child_resource_table_output
        )
        self.command_table["networkcloud cluster baremetalmachinekeyset list"] = List(
            loader=self, table_transformer=transform_child_resource_table_output
        )

    # cluster bmckeyset
    with self.command_group("networkcloud cluster bmckeyset"):
        from .aaz.latest.networkcloud.cluster.bmckeyset import List, Show

        self.command_table["networkcloud cluster bmckeyset show"] = Show(
            loader=self, table_transformer=transform_child_resource_table_output
        )
        self.command_table["networkcloud cluster bmckeyset list"] = List(
            loader=self, table_transformer=transform_child_resource_table_output
        )

    # cluster metricsconfiguration
    with self.command_group("networkcloud cluster metricsconfiguration"):
        from .aaz.latest.networkcloud.cluster.metricsconfiguration import List

        self.command_table["networkcloud cluster metricsconfiguration list"] = List(
            loader=self, table_transformer=transform_child_resource_table_output
        )

        from .operations.cluster.metricsconfiguration._create import Create
        from .operations.cluster.metricsconfiguration._delete import Delete
        from .operations.cluster.metricsconfiguration._show import Show
        from .operations.cluster.metricsconfiguration._update import Update

        self.command_table["networkcloud cluster metricsconfiguration create"] = Create(
            loader=self
        )
        self.command_table["networkcloud cluster metricsconfiguration update"] = Update(
            loader=self
        )
        self.command_table["networkcloud cluster metricsconfiguration delete"] = Delete(
            loader=self
        )
        self.command_table["networkcloud cluster metricsconfiguration show"] = Show(
            loader=self, table_transformer=transform_child_resource_table_output
        )

    # clustermanager
    with self.command_group("networkcloud clustermanager"):
        from .aaz.latest.networkcloud.clustermanager import List, Show

        self.command_table["networkcloud clustermanager show"] = Show(
            loader=self, table_transformer=transform_cluster_manager_table_output
        )
        self.command_table["networkcloud clustermanager list"] = List(
            loader=self, table_transformer=transform_cluster_manager_table_output
        )

    # kubernetescluster
    with self.command_group("networkcloud kubernetescluster"):
        from .aaz.latest.networkcloud.kubernetescluster import List, Show

        self.command_table["networkcloud kubernetescluster show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud kubernetescluster list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

        from .operations.kubernetescluster._create import Create

        self.command_table["networkcloud kubernetescluster create"] = Create(
            loader=self
        )

        from .operations.kubernetescluster._update import Update

        self.command_table["networkcloud kubernetescluster update"] = Update(
            loader=self
        )

    # kubernetescluster agentpool
    with self.command_group("networkcloud kubernetescluster agentpool"):
        from .aaz.latest.networkcloud.kubernetescluster.agentpool import List, Show

        self.command_table["networkcloud kubernetescluster agentpool show"] = Show(
            loader=self, table_transformer=transform_child_resource_table_output
        )
        self.command_table["networkcloud kubernetescluster agentpool list"] = List(
            loader=self, table_transformer=transform_child_resource_table_output
        )

        from .operations.kubernetescluster.agentpool._create import Create

        self.command_table["networkcloud kubernetescluster agentpool create"] = Create(
            loader=self
        )

        from .operations.kubernetescluster.agentpool._update import Update

        self.command_table["networkcloud kubernetescluster agentpool update"] = Update(
            loader=self
        )

    # l2network
    with self.command_group("networkcloud l2network"):
        from .aaz.latest.networkcloud.l2network import List, Show

        self.command_table["networkcloud l2network show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud l2network list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

    # l3network
    with self.command_group("networkcloud l3network"):
        from .aaz.latest.networkcloud.l3network import List, Show

        self.command_table["networkcloud l3network show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud l3network list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

    # rack
    with self.command_group("networkcloud rack"):
        from .aaz.latest.networkcloud.rack import List, Show

        self.command_table["networkcloud rack show"] = Show(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )
        self.command_table["networkcloud rack list"] = List(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )

    # racksku
    with self.command_group("networkcloud racksku"):
        from .aaz.latest.networkcloud.racksku import List, Show

        self.command_table["networkcloud racksku show"] = Show(
            loader=self, table_transformer=transform_rack_sku_table_output
        )
        self.command_table["networkcloud racksku list"] = List(
            loader=self, table_transformer=transform_rack_sku_table_output
        )

    # storageappliance
    with self.command_group("networkcloud storageappliance"):
        from .aaz.latest.networkcloud.storageappliance import List, Show

        self.command_table["networkcloud storageappliance show"] = Show(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )
        self.command_table["networkcloud storageappliance list"] = List(
            loader=self, table_transformer=transform_hydrated_resource_table_output
        )

    # trunkednetwork
    with self.command_group("networkcloud trunkednetwork"):
        from .aaz.latest.networkcloud.trunkednetwork import List, Show

        self.command_table["networkcloud trunkednetwork show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud trunkednetwork list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

    # virtualmachine
    with self.command_group("networkcloud virtualmachine"):
        from .aaz.latest.networkcloud.virtualmachine import List, Show

        self.command_table["networkcloud virtualmachine show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud virtualmachine list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )

        from .operations.virtualmachine._create import Create

        self.command_table["networkcloud virtualmachine create"] = Create(loader=self)

    # virtualmachine console
    with self.command_group("networkcloud virtualmachine console"):
        from .aaz.latest.networkcloud.virtualmachine.console import List

        self.command_table["networkcloud virtualmachine console list"] = List(
            loader=self, table_transformer=transform_child_resource_table_output
        )

        from .operations.virtualmachine.console._create import Create
        from .operations.virtualmachine.console._delete import Delete
        from .operations.virtualmachine.console._show import Show
        from .operations.virtualmachine.console._update import Update

        self.command_table["networkcloud virtualmachine console create"] = Create(
            loader=self
        )
        self.command_table["networkcloud virtualmachine console update"] = Update(
            loader=self
        )
        self.command_table["networkcloud virtualmachine console delete"] = Delete(
            loader=self
        )
        self.command_table["networkcloud virtualmachine console show"] = Show(
            loader=self, table_transformer=transform_child_resource_table_output
        )

    # volume
    with self.command_group("networkcloud volume"):
        from .aaz.latest.networkcloud.volume import List, Show

        self.command_table["networkcloud volume show"] = Show(
            loader=self, table_transformer=transform_resource_table_output
        )
        self.command_table["networkcloud volume list"] = List(
            loader=self, table_transformer=transform_resource_table_output
        )
