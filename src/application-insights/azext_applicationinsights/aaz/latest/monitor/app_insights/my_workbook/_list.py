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
    "monitor app-insights my-workbook list",
)
class List(AAZCommand):
    """List all private workbooks defined within a specified subscription and category.

    :example: List my workbook
        az monitor app-insights my-workbook list  -g rg --category retention
    """

    _aaz_info = {
        "version": "2021-03-08",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.insights/myworkbooks", "2021-03-08"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/myworkbooks", "2021-03-08"],
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
        _args_schema.can_fetch_content = AAZBoolArg(
            options=["--can-fetch-content"],
            help="Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.",
        )
        _args_schema.category = AAZStrArg(
            options=["--category"],
            help="Category of workbook to return.",
            required=True,
            enum={"TSG": "TSG", "performance": "performance", "retention": "retention", "workbook": "workbook"},
        )
        _args_schema.source_id = AAZStrArg(
            options=["--source-id"],
            help="Azure Resource Id that will fetch all linked workbooks.",
        )
        _args_schema.tags = AAZListArg(
            options=["--tags"],
            help="Tags presents on each workbook returned.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id) and has_value(self.ctx.args.category)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.category) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.MyWorkbooksListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.MyWorkbooksListBySubscription(ctx=self.ctx)()
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

    class MyWorkbooksListByResourceGroup(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/myWorkbooks",
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
                    "canFetchContent", self.ctx.args.can_fetch_content,
                ),
                **self.serialize_query_param(
                    "category", self.ctx.args.category,
                    required=True,
                ),
                **self.serialize_query_param(
                    "sourceId", self.ctx.args.source_id,
                ),
                **self.serialize_query_param(
                    "tags", self.ctx.args.tags,
                ),
                **self.serialize_query_param(
                    "api-version", "2021-03-08",
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
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZDictType()
            _element.id = AAZStrType()
            _element.identity = AAZObjectType()
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType()

            etag = cls._schema_on_200.value.Element.etag
            etag.Element = AAZStrType()

            identity = cls._schema_on_200.value.Element.identity
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZObjectType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            user_assigned_identities.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.category = AAZStrType(
                flags={"required": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.serialized_data = AAZStrType(
                serialized_name="serializedData",
                flags={"required": True},
                nullable=True,
            )
            properties.storage_uri = AAZStrType(
                serialized_name="storageUri",
                nullable=True,
            )
            properties.tags = AAZListType()
            properties.time_modified = AAZStrType(
                serialized_name="timeModified",
                flags={"read_only": True},
            )
            properties.user_id = AAZStrType(
                serialized_name="userId",
                flags={"read_only": True},
            )
            properties.version = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.tags
            tags.Element = AAZStrType()

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

    class MyWorkbooksListBySubscription(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/myWorkbooks",
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
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "canFetchContent", self.ctx.args.can_fetch_content,
                ),
                **self.serialize_query_param(
                    "category", self.ctx.args.category,
                    required=True,
                ),
                **self.serialize_query_param(
                    "tags", self.ctx.args.tags,
                ),
                **self.serialize_query_param(
                    "api-version", "2021-03-08",
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
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZDictType()
            _element.id = AAZStrType()
            _element.identity = AAZObjectType()
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType()

            etag = cls._schema_on_200.value.Element.etag
            etag.Element = AAZStrType()

            identity = cls._schema_on_200.value.Element.identity
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZObjectType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            user_assigned_identities.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.category = AAZStrType(
                flags={"required": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.serialized_data = AAZStrType(
                serialized_name="serializedData",
                flags={"required": True},
                nullable=True,
            )
            properties.storage_uri = AAZStrType(
                serialized_name="storageUri",
                nullable=True,
            )
            properties.tags = AAZListType()
            properties.time_modified = AAZStrType(
                serialized_name="timeModified",
                flags={"read_only": True},
            )
            properties.user_id = AAZStrType(
                serialized_name="userId",
                flags={"read_only": True},
            )
            properties.version = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.tags
            tags.Element = AAZStrType()

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


__all__ = ["List"]
