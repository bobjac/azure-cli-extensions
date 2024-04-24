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
    "logic integration-account assembly show",
)
class Show(AAZCommand):
    """Show an assembly for an integration account.

    :example: Show assembly
        az logic integration-account assembly show -g rg --integration-account-name name -n assembly
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/assemblies/{}", "2019-05-01"],
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
        _args_schema.assembly_artifact_name = AAZStrArg(
            options=["-n", "--name", "--assembly-artifact-name"],
            help="The assembly artifact name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountAssembliesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountAssembliesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName}",
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
                    "assemblyArtifactName", self.ctx.args.assembly_artifact_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
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
                    "api-version", "2019-05-01",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.assembly_culture = AAZStrType(
                serialized_name="assemblyCulture",
            )
            properties.assembly_name = AAZStrType(
                serialized_name="assemblyName",
                flags={"required": True},
            )
            properties.assembly_public_key_token = AAZStrType(
                serialized_name="assemblyPublicKeyToken",
            )
            properties.assembly_version = AAZStrType(
                serialized_name="assemblyVersion",
            )
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
            )
            properties.content = AAZStrType()
            properties.content_link = AAZObjectType(
                serialized_name="contentLink",
            )
            properties.content_type = AAZStrType(
                serialized_name="contentType",
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
            )
            properties.metadata = AAZFreeFormDictType()

            content_link = cls._schema_on_200.properties.content_link
            content_link.content_hash = AAZObjectType(
                serialized_name="contentHash",
            )
            content_link.content_size = AAZIntType(
                serialized_name="contentSize",
                flags={"read_only": True},
            )
            content_link.content_version = AAZStrType(
                serialized_name="contentVersion",
                flags={"read_only": True},
            )
            content_link.metadata = AAZObjectType()
            content_link.uri = AAZStrType()

            content_hash = cls._schema_on_200.properties.content_link.content_hash
            content_hash.algorithm = AAZStrType()
            content_hash.value = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
