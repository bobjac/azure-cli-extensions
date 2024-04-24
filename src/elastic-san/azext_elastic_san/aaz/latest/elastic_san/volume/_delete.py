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
    "elastic-san volume delete",
    confirmation="Are you sure you want to perform this operation?",
)
class Delete(AAZCommand):
    """Delete a Volume.

    :example: Delete a Volume.
        az elastic-san volume delete -g "rg" -e "san_name" -v "vg_name" -n "volume_name"

    :example: Delete a volume with its snapshot
        az elastic-san volume delete -g "rg" -e "san_name" -v "vg_name" -n "volume_name" -y --x-ms-delete-snapshots true --x-ms-force-delete true
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elasticsan/elasticsans/{}/volumegroups/{}/volumes/{}", "2023-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.x_ms_delete_snapshots = AAZStrArg(
            options=["--x-ms-delete-snapshots"],
            help="Optional, used to delete snapshots under volume. Allowed value are only true or false. Default value is false.",
            enum={"false": "false", "true": "true"},
        )
        _args_schema.x_ms_force_delete = AAZStrArg(
            options=["--x-ms-force-delete"],
            help="Optional, used to delete volume if active sessions present. Allowed value are only true or false. Default value is false.",
            enum={"false": "false", "true": "true"},
        )
        _args_schema.elastic_san_name = AAZStrArg(
            options=["-e", "--elastic-san", "--elastic-san-name"],
            help="The name of the ElasticSan.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9]+((-|_)[a-z0-9A-Z]+)*$",
                max_length=24,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.volume_group_name = AAZStrArg(
            options=["-v", "--volume-group", "--volume-group-name"],
            help="The name of the VolumeGroup.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9]+((-|_)[a-z0-9A-Z]+)*$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.volume_name = AAZStrArg(
            options=["-n", "--name", "--volume-name"],
            help="The name of the Volume.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9]+(-[a-z0-9A-Z]+)*$",
                max_length=63,
                min_length=3,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VolumesDelete(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class VolumesDelete(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [204]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_204,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}/volumes/{volumeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "elasticSanName", self.ctx.args.elastic_san_name,
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
                **self.serialize_url_param(
                    "volumeGroupName", self.ctx.args.volume_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "volumeName", self.ctx.args.volume_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "x-ms-delete-snapshots", self.ctx.args.x_ms_delete_snapshots,
                ),
                **self.serialize_header_param(
                    "x-ms-force-delete", self.ctx.args.x_ms_force_delete,
                ),
            }
            return parameters

        def on_200(self, session):
            pass

        def on_204(self, session):
            pass


class _DeleteHelper:
    """Helper class for Delete"""


__all__ = ["Delete"]
