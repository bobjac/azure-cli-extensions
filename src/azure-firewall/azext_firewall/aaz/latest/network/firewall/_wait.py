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
    "network firewall wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/azurefirewalls/{}", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Azure Firewall name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AzureFirewallsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class AzureFirewallsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/azureFirewalls/{azureFirewallName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "azureFirewallName", self.ctx.args.name,
                    required=True,
                ),
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
                    "api-version", "2022-01-01",
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
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.zones = AAZListType()

            properties = cls._schema_on_200.properties
            properties.additional_properties = AAZDictType(
                serialized_name="additionalProperties",
            )
            properties.application_rule_collections = AAZListType(
                serialized_name="applicationRuleCollections",
            )
            properties.firewall_policy = AAZObjectType(
                serialized_name="firewallPolicy",
            )
            _WaitHelper._build_schema_sub_resource_read(properties.firewall_policy)
            properties.hub_ip_addresses = AAZObjectType(
                serialized_name="hubIPAddresses",
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.ip_groups = AAZListType(
                serialized_name="ipGroups",
            )
            properties.management_ip_configuration = AAZObjectType(
                serialized_name="managementIpConfiguration",
            )
            _WaitHelper._build_schema_azure_firewall_ip_configuration_read(properties.management_ip_configuration)
            properties.nat_rule_collections = AAZListType(
                serialized_name="natRuleCollections",
            )
            properties.network_rule_collections = AAZListType(
                serialized_name="networkRuleCollections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sku = AAZObjectType()
            properties.threat_intel_mode = AAZStrType(
                serialized_name="threatIntelMode",
            )
            properties.virtual_hub = AAZObjectType(
                serialized_name="virtualHub",
            )
            _WaitHelper._build_schema_sub_resource_read(properties.virtual_hub)

            additional_properties = cls._schema_on_200.properties.additional_properties
            additional_properties.Element = AAZStrType()

            application_rule_collections = cls._schema_on_200.properties.application_rule_collections
            application_rule_collections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.application_rule_collections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.application_rule_collections.Element.properties
            properties.action = AAZObjectType()
            _WaitHelper._build_schema_azure_firewall_rc_action_read(properties.action)
            properties.priority = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rules = AAZListType()

            rules = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element
            _element.description = AAZStrType()
            _element.fqdn_tags = AAZListType(
                serialized_name="fqdnTags",
            )
            _element.name = AAZStrType()
            _element.protocols = AAZListType()
            _element.source_addresses = AAZListType(
                serialized_name="sourceAddresses",
            )
            _element.source_ip_groups = AAZListType(
                serialized_name="sourceIpGroups",
            )
            _element.target_fqdns = AAZListType(
                serialized_name="targetFqdns",
            )

            fqdn_tags = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.fqdn_tags
            fqdn_tags.Element = AAZStrType()

            protocols = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.protocols
            protocols.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.protocols.Element
            _element.port = AAZIntType()
            _element.protocol_type = AAZStrType(
                serialized_name="protocolType",
            )

            source_addresses = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.source_addresses
            source_addresses.Element = AAZStrType()

            source_ip_groups = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.source_ip_groups
            source_ip_groups.Element = AAZStrType()

            target_fqdns = cls._schema_on_200.properties.application_rule_collections.Element.properties.rules.Element.target_fqdns
            target_fqdns.Element = AAZStrType()

            hub_ip_addresses = cls._schema_on_200.properties.hub_ip_addresses
            hub_ip_addresses.private_ip_address = AAZStrType(
                serialized_name="privateIPAddress",
            )
            hub_ip_addresses.public_i_ps = AAZObjectType(
                serialized_name="publicIPs",
            )

            public_i_ps = cls._schema_on_200.properties.hub_ip_addresses.public_i_ps
            public_i_ps.addresses = AAZListType()
            public_i_ps.count = AAZIntType()

            addresses = cls._schema_on_200.properties.hub_ip_addresses.public_i_ps.addresses
            addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.hub_ip_addresses.public_i_ps.addresses.Element
            _element.address = AAZStrType()

            ip_configurations = cls._schema_on_200.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()
            _WaitHelper._build_schema_azure_firewall_ip_configuration_read(ip_configurations.Element)

            ip_groups = cls._schema_on_200.properties.ip_groups
            ip_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ip_groups.Element
            _element.change_number = AAZStrType(
                serialized_name="changeNumber",
                flags={"read_only": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )

            nat_rule_collections = cls._schema_on_200.properties.nat_rule_collections
            nat_rule_collections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.nat_rule_collections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.nat_rule_collections.Element.properties
            properties.action = AAZObjectType()
            properties.priority = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rules = AAZListType()

            action = cls._schema_on_200.properties.nat_rule_collections.Element.properties.action
            action.type = AAZStrType()

            rules = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element
            _element.description = AAZStrType()
            _element.destination_addresses = AAZListType(
                serialized_name="destinationAddresses",
            )
            _element.destination_ports = AAZListType(
                serialized_name="destinationPorts",
            )
            _element.name = AAZStrType()
            _element.protocols = AAZListType()
            _element.source_addresses = AAZListType(
                serialized_name="sourceAddresses",
            )
            _element.source_ip_groups = AAZListType(
                serialized_name="sourceIpGroups",
            )
            _element.translated_address = AAZStrType(
                serialized_name="translatedAddress",
            )
            _element.translated_fqdn = AAZStrType(
                serialized_name="translatedFqdn",
            )
            _element.translated_port = AAZStrType(
                serialized_name="translatedPort",
            )

            destination_addresses = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element.destination_addresses
            destination_addresses.Element = AAZStrType()

            destination_ports = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element.destination_ports
            destination_ports.Element = AAZStrType()

            protocols = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element.protocols
            protocols.Element = AAZStrType()

            source_addresses = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element.source_addresses
            source_addresses.Element = AAZStrType()

            source_ip_groups = cls._schema_on_200.properties.nat_rule_collections.Element.properties.rules.Element.source_ip_groups
            source_ip_groups.Element = AAZStrType()

            network_rule_collections = cls._schema_on_200.properties.network_rule_collections
            network_rule_collections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_rule_collections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.network_rule_collections.Element.properties
            properties.action = AAZObjectType()
            _WaitHelper._build_schema_azure_firewall_rc_action_read(properties.action)
            properties.priority = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rules = AAZListType()

            rules = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element
            _element.description = AAZStrType()
            _element.destination_addresses = AAZListType(
                serialized_name="destinationAddresses",
            )
            _element.destination_fqdns = AAZListType(
                serialized_name="destinationFqdns",
            )
            _element.destination_ip_groups = AAZListType(
                serialized_name="destinationIpGroups",
            )
            _element.destination_ports = AAZListType(
                serialized_name="destinationPorts",
            )
            _element.name = AAZStrType()
            _element.protocols = AAZListType()
            _element.source_addresses = AAZListType(
                serialized_name="sourceAddresses",
            )
            _element.source_ip_groups = AAZListType(
                serialized_name="sourceIpGroups",
            )

            destination_addresses = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.destination_addresses
            destination_addresses.Element = AAZStrType()

            destination_fqdns = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.destination_fqdns
            destination_fqdns.Element = AAZStrType()

            destination_ip_groups = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.destination_ip_groups
            destination_ip_groups.Element = AAZStrType()

            destination_ports = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.destination_ports
            destination_ports.Element = AAZStrType()

            protocols = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.protocols
            protocols.Element = AAZStrType()

            source_addresses = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.source_addresses
            source_addresses.Element = AAZStrType()

            source_ip_groups = cls._schema_on_200.properties.network_rule_collections.Element.properties.rules.Element.source_ip_groups
            source_ip_groups.Element = AAZStrType()

            sku = cls._schema_on_200.properties.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_azure_firewall_ip_configuration_read = None

    @classmethod
    def _build_schema_azure_firewall_ip_configuration_read(cls, _schema):
        if cls._schema_azure_firewall_ip_configuration_read is not None:
            _schema.etag = cls._schema_azure_firewall_ip_configuration_read.etag
            _schema.id = cls._schema_azure_firewall_ip_configuration_read.id
            _schema.name = cls._schema_azure_firewall_ip_configuration_read.name
            _schema.properties = cls._schema_azure_firewall_ip_configuration_read.properties
            _schema.type = cls._schema_azure_firewall_ip_configuration_read.type
            return

        cls._schema_azure_firewall_ip_configuration_read = _schema_azure_firewall_ip_configuration_read = AAZObjectType()

        azure_firewall_ip_configuration_read = _schema_azure_firewall_ip_configuration_read
        azure_firewall_ip_configuration_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        azure_firewall_ip_configuration_read.id = AAZStrType()
        azure_firewall_ip_configuration_read.name = AAZStrType()
        azure_firewall_ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        azure_firewall_ip_configuration_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_azure_firewall_ip_configuration_read.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_sub_resource_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_sub_resource_read(properties.subnet)

        _schema.etag = cls._schema_azure_firewall_ip_configuration_read.etag
        _schema.id = cls._schema_azure_firewall_ip_configuration_read.id
        _schema.name = cls._schema_azure_firewall_ip_configuration_read.name
        _schema.properties = cls._schema_azure_firewall_ip_configuration_read.properties
        _schema.type = cls._schema_azure_firewall_ip_configuration_read.type

    _schema_azure_firewall_rc_action_read = None

    @classmethod
    def _build_schema_azure_firewall_rc_action_read(cls, _schema):
        if cls._schema_azure_firewall_rc_action_read is not None:
            _schema.type = cls._schema_azure_firewall_rc_action_read.type
            return

        cls._schema_azure_firewall_rc_action_read = _schema_azure_firewall_rc_action_read = AAZObjectType()

        azure_firewall_rc_action_read = _schema_azure_firewall_rc_action_read
        azure_firewall_rc_action_read.type = AAZStrType()

        _schema.type = cls._schema_azure_firewall_rc_action_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Wait"]
