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
    "workloads monitor sap-landscape-monitor list",
    is_preview=True,
)
class List(AAZCommand):
    """List configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name.

    :example: List configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name.
        az workloads monitor sap-landscape-monitor list -g <RG-NAME> --monitor-name <monitor-name>
    """

    _aaz_info = {
        "version": "2023-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/monitors/{}/saplandscapemonitor", "2023-04-01"],
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
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Name of the SAP monitor resource.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SapLandscapeMonitorList(ctx=self.ctx)()
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

    class SapLandscapeMonitorList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}/sapLandscapeMonitor",
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
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2023-04-01",
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
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.grouping = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.top_metrics_thresholds = AAZListType(
                serialized_name="topMetricsThresholds",
            )

            grouping = cls._schema_on_200.value.Element.properties.grouping
            grouping.landscape = AAZListType()
            grouping.sap_application = AAZListType(
                serialized_name="sapApplication",
            )

            landscape = cls._schema_on_200.value.Element.properties.grouping.landscape
            landscape.Element = AAZObjectType()
            _ListHelper._build_schema_sap_landscape_monitor_sid_mapping_read(landscape.Element)

            sap_application = cls._schema_on_200.value.Element.properties.grouping.sap_application
            sap_application.Element = AAZObjectType()
            _ListHelper._build_schema_sap_landscape_monitor_sid_mapping_read(sap_application.Element)

            top_metrics_thresholds = cls._schema_on_200.value.Element.properties.top_metrics_thresholds
            top_metrics_thresholds.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.top_metrics_thresholds.Element
            _element.green = AAZFloatType()
            _element.name = AAZStrType()
            _element.red = AAZFloatType()
            _element.yellow = AAZFloatType()

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

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_sap_landscape_monitor_sid_mapping_read = None

    @classmethod
    def _build_schema_sap_landscape_monitor_sid_mapping_read(cls, _schema):
        if cls._schema_sap_landscape_monitor_sid_mapping_read is not None:
            _schema.name = cls._schema_sap_landscape_monitor_sid_mapping_read.name
            _schema.top_sid = cls._schema_sap_landscape_monitor_sid_mapping_read.top_sid
            return

        cls._schema_sap_landscape_monitor_sid_mapping_read = _schema_sap_landscape_monitor_sid_mapping_read = AAZObjectType()

        sap_landscape_monitor_sid_mapping_read = _schema_sap_landscape_monitor_sid_mapping_read
        sap_landscape_monitor_sid_mapping_read.name = AAZStrType()
        sap_landscape_monitor_sid_mapping_read.top_sid = AAZListType(
            serialized_name="topSid",
        )

        top_sid = _schema_sap_landscape_monitor_sid_mapping_read.top_sid
        top_sid.Element = AAZStrType()

        _schema.name = cls._schema_sap_landscape_monitor_sid_mapping_read.name
        _schema.top_sid = cls._schema_sap_landscape_monitor_sid_mapping_read.top_sid


__all__ = ["List"]
