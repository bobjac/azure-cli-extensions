# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

"""
BMCKeySet tests scenarios
"""

from azure.cli.testsdk import ScenarioTest

from .config import CONFIG


def setup_scenario1(test):
    """Env setup_scenario1"""
    pass


def cleanup_scenario1(test):
    """Env cleanup_scenario1"""
    pass


def call_scenario1(test):
    """# Testcase: scenario1"""
    setup_scenario1(test)
    step_create(
        test,
        checks=[
            test.check("name", "{name}"),
            test.check("provisioningState", "Succeeded"),
        ],
    )
    step_update(
        test,
        checks=[
            test.check("tags", "{tagsUpdate}"),
            test.check("provisioningState", "Succeeded"),
        ],
    )
    step_show(test, checks=[])
    step_list_resource_group(test, checks=[])
    step_delete(test, checks=[])
    cleanup_scenario1(test)


def step_create(test, checks=None):
    """BMCKeySet create operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkcloud cluster bmckeyset create --name {name} --cluster-name {clusterName} "
        '--extended-location name={extendedLocation} type="CustomLocation" '
        "--location {location} --azure-group-id {azureGroupId} --expiration {expiration} "
        "--privilege-level {privilegeLevel} --user-list {userList} "
        "--tags {tags} --resource-group {rg}",
        checks=checks,
    )


def step_show(test, checks=None):
    """BMCKeySet show operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkcloud cluster bmckeyset show --name {name} --cluster-name {clusterName} --resource-group {rg}"
    )


def step_delete(test, checks=None):
    """BMCKeySet delete operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkcloud cluster bmckeyset  delete --name {name} --cluster-name {clusterName} --resource-group {rg} -y"
    )


def step_list_resource_group(test, checks=None):
    """BMCKeySet list by resource group operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkcloud cluster bmckeyset list --cluster-name {clusterName} --resource-group {rg}"
    )


def step_update(test, checks=None):
    """BMCKeySet update operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkcloud cluster bmckeyset update --name {name} --cluster-name {clusterName} "
        "--tags {tagsUpdate} --user-list {userListUpdate} --expiration {expirationUpdate} "
        "--resource-group {rg}"
    )


class BMCKeySetScenarioTest(ScenarioTest):
    """BMCKeySet scenario test"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update(
            {
                # Autogenerated resource group is not used in this scenario as it depeneds on the
                # parent resource cluster to be present in the RG
                "rg": CONFIG.get("BMC_KEYSET", "resource_group"),
                "name": self.create_random_name(prefix="cli-test-bmcks-", length=24),
                "location": CONFIG.get("BMC_KEYSET", "location"),
                "extendedLocation": CONFIG.get("BMC_KEYSET", "extended_location"),
                "tags": CONFIG.get("BMC_KEYSET", "tags"),
                "tagsUpdate": CONFIG.get("BMC_KEYSET", "tags_update"),
                "azureGroupId": CONFIG.get("BMC_KEYSET", "azure_group_id"),
                "expiration": CONFIG.get("BMC_KEYSET", "expiration"),
                "expirationUpdate": CONFIG.get("BMC_KEYSET", "expirationUpdate"),
                "privilegeLevel": CONFIG.get("BMC_KEYSET", "privilege_level"),
                "userList": CONFIG.get("BMC_KEYSET", "user_list"),
                "userListUpdate": CONFIG.get("BMC_KEYSET", "user_list_update"),
                "clusterName": CONFIG.get("BMC_KEYSET", "cluster_name"),
            }
        )

    def test_bmckeyset_scenario1(self):
        """test scenario for BMCKeySet CRUD operations"""
        call_scenario1(self)
