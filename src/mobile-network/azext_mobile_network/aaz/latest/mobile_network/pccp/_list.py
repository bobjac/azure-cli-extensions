# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "mobile-network pccp list",
)
class List(AAZCommand):
    """List all the packet core control planes in a subscription.

    :example: List Packet Core Control Plane by resource group
        az mobile-network pccp list -g rg
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.mobilenetwork/packetcorecontrolplanes", "2023-09-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.mobilenetwork/packetcorecontrolplanes", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.PacketCoreControlPlanesListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.PacketCoreControlPlanesListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class PacketCoreControlPlanesListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.control_plane_access_interface = AAZObjectType(
                serialized_name="controlPlaneAccessInterface",
                flags={"required": True},
            )
            properties.control_plane_access_virtual_ipv4_addresses = AAZListType(
                serialized_name="controlPlaneAccessVirtualIpv4Addresses",
            )
            properties.core_network_technology = AAZStrType(
                serialized_name="coreNetworkTechnology",
            )
            properties.diagnostics_upload = AAZObjectType(
                serialized_name="diagnosticsUpload",
            )
            properties.event_hub = AAZObjectType(
                serialized_name="eventHub",
            )
            properties.installation = AAZObjectType()
            properties.installed_version = AAZStrType(
                serialized_name="installedVersion",
                flags={"read_only": True},
            )
            properties.interop_settings = AAZObjectType(
                serialized_name="interopSettings",
            )
            properties.local_diagnostics_access = AAZObjectType(
                serialized_name="localDiagnosticsAccess",
                flags={"required": True},
            )
            properties.platform = AAZObjectType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rollback_version = AAZStrType(
                serialized_name="rollbackVersion",
                flags={"read_only": True},
            )
            properties.signaling = AAZObjectType()
            properties.sites = AAZListType(
                flags={"required": True},
            )
            properties.sku = AAZStrType(
                flags={"required": True},
            )
            properties.ue_mtu = AAZIntType(
                serialized_name="ueMtu",
            )
            properties.version = AAZStrType()

            control_plane_access_interface = cls._schema_on_200.value.Element.properties.control_plane_access_interface
            control_plane_access_interface.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            control_plane_access_interface.ipv4_gateway = AAZStrType(
                serialized_name="ipv4Gateway",
            )
            control_plane_access_interface.ipv4_subnet = AAZStrType(
                serialized_name="ipv4Subnet",
            )
            control_plane_access_interface.name = AAZStrType()

            control_plane_access_virtual_ipv4_addresses = cls._schema_on_200.value.Element.properties.control_plane_access_virtual_ipv4_addresses
            control_plane_access_virtual_ipv4_addresses.Element = AAZStrType()

            diagnostics_upload = cls._schema_on_200.value.Element.properties.diagnostics_upload
            diagnostics_upload.storage_account_container_url = AAZStrType(
                serialized_name="storageAccountContainerUrl",
                flags={"required": True},
            )

            event_hub = cls._schema_on_200.value.Element.properties.event_hub
            event_hub.id = AAZStrType(
                flags={"required": True},
            )
            event_hub.reporting_interval = AAZIntType(
                serialized_name="reportingInterval",
            )

            installation = cls._schema_on_200.value.Element.properties.installation
            installation.desired_state = AAZStrType(
                serialized_name="desiredState",
            )
            installation.operation = AAZObjectType()
            installation.reasons = AAZListType(
                flags={"read_only": True},
            )
            installation.reinstall_required = AAZStrType(
                serialized_name="reinstallRequired",
            )
            installation.state = AAZStrType()

            operation = cls._schema_on_200.value.Element.properties.installation.operation
            operation.id = AAZStrType(
                flags={"required": True},
            )

            reasons = cls._schema_on_200.value.Element.properties.installation.reasons
            reasons.Element = AAZStrType()

            local_diagnostics_access = cls._schema_on_200.value.Element.properties.local_diagnostics_access
            local_diagnostics_access.authentication_type = AAZStrType(
                serialized_name="authenticationType",
                flags={"required": True},
            )
            local_diagnostics_access.https_server_certificate = AAZObjectType(
                serialized_name="httpsServerCertificate",
            )

            https_server_certificate = cls._schema_on_200.value.Element.properties.local_diagnostics_access.https_server_certificate
            https_server_certificate.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
                flags={"required": True},
            )
            https_server_certificate.provisioning = AAZObjectType()

            provisioning = cls._schema_on_200.value.Element.properties.local_diagnostics_access.https_server_certificate.provisioning
            provisioning.reason = AAZStrType(
                flags={"read_only": True},
            )
            provisioning.state = AAZStrType(
                flags={"read_only": True},
            )

            platform = cls._schema_on_200.value.Element.properties.platform
            platform.azure_stack_edge_device = AAZObjectType(
                serialized_name="azureStackEdgeDevice",
            )
            _ListHelper._build_schema_azure_stack_edge_device_resource_id_read(platform.azure_stack_edge_device)
            platform.azure_stack_edge_devices = AAZListType(
                serialized_name="azureStackEdgeDevices",
                flags={"read_only": True},
            )
            platform.azure_stack_hci_cluster = AAZObjectType(
                serialized_name="azureStackHciCluster",
            )
            platform.connected_cluster = AAZObjectType(
                serialized_name="connectedCluster",
            )
            platform.custom_location = AAZObjectType(
                serialized_name="customLocation",
            )
            platform.type = AAZStrType(
                flags={"required": True},
            )

            azure_stack_edge_devices = cls._schema_on_200.value.Element.properties.platform.azure_stack_edge_devices
            azure_stack_edge_devices.Element = AAZObjectType()
            _ListHelper._build_schema_azure_stack_edge_device_resource_id_read(azure_stack_edge_devices.Element)

            azure_stack_hci_cluster = cls._schema_on_200.value.Element.properties.platform.azure_stack_hci_cluster
            azure_stack_hci_cluster.id = AAZStrType(
                flags={"required": True},
            )

            connected_cluster = cls._schema_on_200.value.Element.properties.platform.connected_cluster
            connected_cluster.id = AAZStrType(
                flags={"required": True},
            )

            custom_location = cls._schema_on_200.value.Element.properties.platform.custom_location
            custom_location.id = AAZStrType(
                flags={"required": True},
            )

            signaling = cls._schema_on_200.value.Element.properties.signaling
            signaling.nas_reroute = AAZObjectType(
                serialized_name="nasReroute",
            )

            nas_reroute = cls._schema_on_200.value.Element.properties.signaling.nas_reroute
            nas_reroute.macro_mme_group_id = AAZIntType(
                serialized_name="macroMmeGroupId",
                flags={"required": True},
            )

            sites = cls._schema_on_200.value.Element.properties.sites
            sites.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sites.Element
            _element.id = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class PacketCoreControlPlanesListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.control_plane_access_interface = AAZObjectType(
                serialized_name="controlPlaneAccessInterface",
                flags={"required": True},
            )
            properties.control_plane_access_virtual_ipv4_addresses = AAZListType(
                serialized_name="controlPlaneAccessVirtualIpv4Addresses",
            )
            properties.core_network_technology = AAZStrType(
                serialized_name="coreNetworkTechnology",
            )
            properties.diagnostics_upload = AAZObjectType(
                serialized_name="diagnosticsUpload",
            )
            properties.event_hub = AAZObjectType(
                serialized_name="eventHub",
            )
            properties.installation = AAZObjectType()
            properties.installed_version = AAZStrType(
                serialized_name="installedVersion",
                flags={"read_only": True},
            )
            properties.interop_settings = AAZObjectType(
                serialized_name="interopSettings",
            )
            properties.local_diagnostics_access = AAZObjectType(
                serialized_name="localDiagnosticsAccess",
                flags={"required": True},
            )
            properties.platform = AAZObjectType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rollback_version = AAZStrType(
                serialized_name="rollbackVersion",
                flags={"read_only": True},
            )
            properties.signaling = AAZObjectType()
            properties.sites = AAZListType(
                flags={"required": True},
            )
            properties.sku = AAZStrType(
                flags={"required": True},
            )
            properties.ue_mtu = AAZIntType(
                serialized_name="ueMtu",
            )
            properties.version = AAZStrType()

            control_plane_access_interface = cls._schema_on_200.value.Element.properties.control_plane_access_interface
            control_plane_access_interface.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )
            control_plane_access_interface.ipv4_gateway = AAZStrType(
                serialized_name="ipv4Gateway",
            )
            control_plane_access_interface.ipv4_subnet = AAZStrType(
                serialized_name="ipv4Subnet",
            )
            control_plane_access_interface.name = AAZStrType()

            control_plane_access_virtual_ipv4_addresses = cls._schema_on_200.value.Element.properties.control_plane_access_virtual_ipv4_addresses
            control_plane_access_virtual_ipv4_addresses.Element = AAZStrType()

            diagnostics_upload = cls._schema_on_200.value.Element.properties.diagnostics_upload
            diagnostics_upload.storage_account_container_url = AAZStrType(
                serialized_name="storageAccountContainerUrl",
                flags={"required": True},
            )

            event_hub = cls._schema_on_200.value.Element.properties.event_hub
            event_hub.id = AAZStrType(
                flags={"required": True},
            )
            event_hub.reporting_interval = AAZIntType(
                serialized_name="reportingInterval",
            )

            installation = cls._schema_on_200.value.Element.properties.installation
            installation.desired_state = AAZStrType(
                serialized_name="desiredState",
            )
            installation.operation = AAZObjectType()
            installation.reasons = AAZListType(
                flags={"read_only": True},
            )
            installation.reinstall_required = AAZStrType(
                serialized_name="reinstallRequired",
            )
            installation.state = AAZStrType()

            operation = cls._schema_on_200.value.Element.properties.installation.operation
            operation.id = AAZStrType(
                flags={"required": True},
            )

            reasons = cls._schema_on_200.value.Element.properties.installation.reasons
            reasons.Element = AAZStrType()

            local_diagnostics_access = cls._schema_on_200.value.Element.properties.local_diagnostics_access
            local_diagnostics_access.authentication_type = AAZStrType(
                serialized_name="authenticationType",
                flags={"required": True},
            )
            local_diagnostics_access.https_server_certificate = AAZObjectType(
                serialized_name="httpsServerCertificate",
            )

            https_server_certificate = cls._schema_on_200.value.Element.properties.local_diagnostics_access.https_server_certificate
            https_server_certificate.certificate_url = AAZStrType(
                serialized_name="certificateUrl",
                flags={"required": True},
            )
            https_server_certificate.provisioning = AAZObjectType()

            provisioning = cls._schema_on_200.value.Element.properties.local_diagnostics_access.https_server_certificate.provisioning
            provisioning.reason = AAZStrType(
                flags={"read_only": True},
            )
            provisioning.state = AAZStrType(
                flags={"read_only": True},
            )

            platform = cls._schema_on_200.value.Element.properties.platform
            platform.azure_stack_edge_device = AAZObjectType(
                serialized_name="azureStackEdgeDevice",
            )
            _ListHelper._build_schema_azure_stack_edge_device_resource_id_read(platform.azure_stack_edge_device)
            platform.azure_stack_edge_devices = AAZListType(
                serialized_name="azureStackEdgeDevices",
                flags={"read_only": True},
            )
            platform.azure_stack_hci_cluster = AAZObjectType(
                serialized_name="azureStackHciCluster",
            )
            platform.connected_cluster = AAZObjectType(
                serialized_name="connectedCluster",
            )
            platform.custom_location = AAZObjectType(
                serialized_name="customLocation",
            )
            platform.type = AAZStrType(
                flags={"required": True},
            )

            azure_stack_edge_devices = cls._schema_on_200.value.Element.properties.platform.azure_stack_edge_devices
            azure_stack_edge_devices.Element = AAZObjectType()
            _ListHelper._build_schema_azure_stack_edge_device_resource_id_read(azure_stack_edge_devices.Element)

            azure_stack_hci_cluster = cls._schema_on_200.value.Element.properties.platform.azure_stack_hci_cluster
            azure_stack_hci_cluster.id = AAZStrType(
                flags={"required": True},
            )

            connected_cluster = cls._schema_on_200.value.Element.properties.platform.connected_cluster
            connected_cluster.id = AAZStrType(
                flags={"required": True},
            )

            custom_location = cls._schema_on_200.value.Element.properties.platform.custom_location
            custom_location.id = AAZStrType(
                flags={"required": True},
            )

            signaling = cls._schema_on_200.value.Element.properties.signaling
            signaling.nas_reroute = AAZObjectType(
                serialized_name="nasReroute",
            )

            nas_reroute = cls._schema_on_200.value.Element.properties.signaling.nas_reroute
            nas_reroute.macro_mme_group_id = AAZIntType(
                serialized_name="macroMmeGroupId",
                flags={"required": True},
            )

            sites = cls._schema_on_200.value.Element.properties.sites
            sites.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sites.Element
            _element.id = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_azure_stack_edge_device_resource_id_read = None

    @classmethod
    def _build_schema_azure_stack_edge_device_resource_id_read(cls, _schema):
        if cls._schema_azure_stack_edge_device_resource_id_read is not None:
            _schema.id = cls._schema_azure_stack_edge_device_resource_id_read.id
            return

        cls._schema_azure_stack_edge_device_resource_id_read = _schema_azure_stack_edge_device_resource_id_read = AAZObjectType()

        azure_stack_edge_device_resource_id_read = _schema_azure_stack_edge_device_resource_id_read
        azure_stack_edge_device_resource_id_read.id = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_azure_stack_edge_device_resource_id_read.id


__all__ = ["List"]
