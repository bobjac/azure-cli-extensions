# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=line-too-long

from uuid import uuid4
from knack.log import get_logger

from azure.cli.core.commands import AzCliCommand
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.models import RoleAssignmentCreateParameters, PrincipalType
from azure.mgmt.kubernetesconfiguration import SourceControlConfigurationClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.kubernetesconfiguration.models import Extension, Identity
from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest

from .common import KUBERNETES_RUNTIME_FPA_APP_ID, KUBERNETES_RUNTIME_RP, ConnectedClusterResourceId, query_rp_oid


logger = get_logger(__name__)


# https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#kubernetes-extension-contributor
KUBERNETES_EXTENSION_CONTRIBUTOR_ROLE_ID = "/providers/Microsoft.Authorization/roleDefinitions/85cb6faf-e071-4c9b-8136-154b5a04f717"
STORAGE_CLASS_CONTRIBUTOR_ROLE_ID = "/providers/Microsoft.Authorization/roleDefinitions/0cd9749a-3aaf-4ae5-8803-bd217705bf3b"
STORAGE_CLASS_EXTENSION_NAME = "arc-k8s-storage-class"
STORAGE_CLASS_EXTENSION_TYPE = "Microsoft.ManagedStorageClass"


def enable_storage_class(cmd: AzCliCommand, resource_uri: str):
    """
    Enable storage class service in a connected cluster


    :param resource_uri: The resource uri of the connected cluster
    """

    resource_id = ConnectedClusterResourceId.parse(resource_uri)

    print(f"Register Kubernetes Runtime RP in subscription {resource_id.subscription_id}...")
    resource_management_client: ResourceManagementClient = get_mgmt_service_client(cmd.cli_ctx, ResourceManagementClient, subscription_id=resource_id.subscription_id)

    resource_management_client.providers.register(
        resource_provider_namespace=KUBERNETES_RUNTIME_RP
    )

    print(f"Installing Storage class Arc Extension in cluster {resource_id.cluster_name}...")

    object_id = query_rp_oid(cmd)
    logger.info("Found Kubernetes Runtime RP SP in tenant with object id %s", object_id)

    source_control_configuration_client: SourceControlConfigurationClient = get_mgmt_service_client(cmd.cli_ctx, SourceControlConfigurationClient)

    lro = source_control_configuration_client.extensions.begin_create(
        resource_group_name=resource_id.resource_group,
        cluster_rp="Microsoft.Kubernetes",
        cluster_resource_name="connectedClusters",
        cluster_name=resource_id.cluster_name,
        extension_name=STORAGE_CLASS_EXTENSION_NAME,
        extension=Extension(
            identity=Identity(
                type="SystemAssigned"
            ),
            extension_type=STORAGE_CLASS_EXTENSION_TYPE,
            release_train="dev",
            configuration_settings={
                "k8sRuntimeFpaObjectId": object_id,
            },
        )
    )

    # Prevent blocking KeyboardInterrupt
    while not lro.done():
        lro.wait(1)

    extension = lro.result()

    authorization_management_client: AuthorizationManagementClient = get_mgmt_service_client(cmd.cli_ctx, AuthorizationManagementClient)

    print("Assign the extension with Storage Class Contributor role under the cluster scope...")
    sc_contributor_role_assignment = authorization_management_client.role_assignments.create(
        scope=resource_id.resource_uri,
        role_assignment_name=str(uuid4()),
        # pylint: disable=missing-kwoa
        parameters=RoleAssignmentCreateParameters(
            role_definition_id=STORAGE_CLASS_CONTRIBUTOR_ROLE_ID,
            principal_id=extension.identity.principal_id,
            principal_type=PrincipalType.SERVICE_PRINCIPAL
        ),
    )

    print("Assign Storage Class RP with Kubernetes Extension Contributor role under the cluster scope...")
    k8s_extension_contributor_role_assignment = authorization_management_client.role_assignments.create(
        scope=resource_id.resource_uri,
        role_assignment_name=str(uuid4()),
        # pylint: disable=missing-kwoa
        parameters=RoleAssignmentCreateParameters(
            role_definition_id=KUBERNETES_EXTENSION_CONTRIBUTOR_ROLE_ID,
            principal_id=KUBERNETES_RUNTIME_FPA_APP_ID,
            principal_type=PrincipalType.SERVICE_PRINCIPAL,
        ),
    )

    return {
        "extension": extension,
        "storage_class_contributor_role_assignment": sc_contributor_role_assignment,
        "kubernetes_extension_contributor_role_assignment": k8s_extension_contributor_role_assignment,
    }


def disable_storage_class(cmd: AzCliCommand, resource_uri: str):
    """
    Disable storage class service in a connected cluster


    :param resource_uri: The resource uri of the connected cluster
    """

    resource_id = ConnectedClusterResourceId.parse(resource_uri)

    print(f"Uninstall Storage class Arc Extension in cluster {resource_id.cluster_name}...")
    source_control_configuration_client: SourceControlConfigurationClient = get_mgmt_service_client(cmd.cli_ctx, SourceControlConfigurationClient)

    extension = source_control_configuration_client.extensions.get(
        resource_group_name=resource_id.resource_group,
        cluster_rp="Microsoft.Kubernetes",
        cluster_resource_name="connectedClusters",
        cluster_name=resource_id.cluster_name,
        extension_name=STORAGE_CLASS_EXTENSION_NAME,
    )

    delete_lro = source_control_configuration_client.extensions.begin_delete(
        resource_group_name=resource_id.resource_group,
        cluster_rp="Microsoft.Kubernetes",
        cluster_resource_name="connectedClusters",
        cluster_name=resource_id.cluster_name,
        extension_name=STORAGE_CLASS_EXTENSION_NAME,
    )

    # Prevent blocking KeyboardInterrupt
    while not delete_lro.done():
        delete_lro.wait(1)

    print("Delete role assignment of the extension identity with Storage Class Contributor role under the cluster scope..")

    authorization_management_client: AuthorizationManagementClient = get_mgmt_service_client(cmd.cli_ctx, AuthorizationManagementClient)
    resource_graph_client: ResourceGraphClient = get_mgmt_service_client(cmd.cli_ctx, ResourceGraphClient, subscription_bound=False)

    sc_contributor_query_response = resource_graph_client.resources(QueryRequest(
        subscriptions=[resource_id.subscription_id],
        query=f"""
    authorizationresources
    | where properties.principalId =~ "{extension.identity.principal_id}" and properties.roleDefinitionId =~ "{STORAGE_CLASS_CONTRIBUTOR_ROLE_ID}" and properties.scope =~ "{resource_uri}"
    | limit 1
        """
    ))

    sc_contributor_role_assignment = None
    if sc_contributor_query_response.total_records == 1:
        sc_contributor_role_assignment = authorization_management_client.role_assignments.delete_by_id(
            role_assignment_id=sc_contributor_query_response.data[0]["id"],
        )
    else:
        print("No role assignment found for the extension identity with Storage Class Contributor role under the cluster scope.")

    print("Delete role assignment for storage class RP with Kubernetes Extension Contributor role under the cluster scope...")

    k8s_extension_contributor_query_response = resource_graph_client.resources(QueryRequest(
        subscriptions=[resource_id.subscription_id],
        query=f"""
    authorizationresources
    | where properties.principalId =~ "{KUBERNETES_RUNTIME_FPA_APP_ID}" and properties.roleDefinitionId =~ "{KUBERNETES_EXTENSION_CONTRIBUTOR_ROLE_ID}" and properties.scope =~ "{resource_uri}"
    | limit 1
        """
    ))

    k8s_extension_contributor_role_assignment = None
    if k8s_extension_contributor_query_response.total_records == 1:
        k8s_extension_contributor_role_assignment = authorization_management_client.role_assignments.delete_by_id(
            role_assignment_id=k8s_extension_contributor_query_response.data[0]["id"],
        )
    else:
        print("No role assignment found for storage class RP with Kubernetes Extension Contributor role under the cluster scope.")

    return {
        "extension": extension,
        "storage_class_contributor_role_assignment": sc_contributor_role_assignment,
        "kubernetes_extension_contributor_role_assignment": k8s_extension_contributor_role_assignment,
    }
