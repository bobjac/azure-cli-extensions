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
    "network vhub route-map rule add",
)
class Add(AAZCommand):
    """Add route map rule

    :example: Add rule to route map
        az network vhub route-map rule add --name rule-name -g rg --route-map-name routemap-name --vhub-name vhub-name --match-criteria "[{matchCondition:Contains,routePrefix:[10.0.0.1/8]}]" --actions "[{type:Add,parameters:[{asPath:[22335]}]}]" --next-step Continue
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualhubs/{}/routemaps/{}", "2022-05-01", "properties.rules[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.route_map_name = AAZStrArg(
            options=["--route-map-name"],
            help="The name of the RouteMap.",
            required=True,
        )
        _args_schema.vhub_name = AAZStrArg(
            options=["--vhub-name"],
            help="The name of the VirtualHub containing the RouteMap.",
            required=True,
        )
        _args_schema.rule_index = AAZIntArg(
            options=["--rule-index"],
            help="The index of the route map rule",
        )

        # define Arg Group "RouteMapParameters.properties.rules[]"

        _args_schema = cls._args_schema
        _args_schema.actions = AAZListArg(
            options=["--actions"],
            arg_group="RouteMapParameters.properties.rules[]",
            help="List of actions which will be applied on a match.",
        )
        _args_schema.match_criteria = AAZListArg(
            options=["--match-criteria"],
            arg_group="RouteMapParameters.properties.rules[]",
            help="List of matching criterion which will be applied to traffic.",
        )
        _args_schema.name = AAZStrArg(
            options=["--name"],
            arg_group="RouteMapParameters.properties.rules[]",
            help="The unique name for the rule.",
        )
        _args_schema.next_step = AAZStrArg(
            options=["--next-step"],
            arg_group="RouteMapParameters.properties.rules[]",
            help="Next step after rule is evaluated. Current supported behaviors are 'Continue'(to next rule) and 'Terminate'.",
            enum={"Continue": "Continue", "Terminate": "Terminate", "Unknown": "Unknown"},
        )

        actions = cls._args_schema.actions
        actions.Element = AAZObjectArg()

        _element = cls._args_schema.actions.Element
        _element.parameters = AAZListArg(
            options=["parameters"],
            help="List of parameters relevant to the action.For instance if type is drop then parameters has list of prefixes to be dropped.If type is add, parameters would have list of ASN numbers to be added",
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="Type of action to be taken. Supported types are 'Remove', 'Add', 'Replace', and 'Drop.'",
            enum={"Add": "Add", "Drop": "Drop", "Remove": "Remove", "Replace": "Replace", "Unknown": "Unknown"},
        )

        parameters = cls._args_schema.actions.Element.parameters
        parameters.Element = AAZObjectArg()

        _element = cls._args_schema.actions.Element.parameters.Element
        _element.as_path = AAZListArg(
            options=["as-path"],
            help="List of AS paths.",
        )
        _element.community = AAZListArg(
            options=["community"],
            help="List of BGP communities.",
        )
        _element.route_prefix = AAZListArg(
            options=["route-prefix"],
            help="List of route prefixes.",
        )

        as_path = cls._args_schema.actions.Element.parameters.Element.as_path
        as_path.Element = AAZStrArg()

        community = cls._args_schema.actions.Element.parameters.Element.community
        community.Element = AAZStrArg()

        route_prefix = cls._args_schema.actions.Element.parameters.Element.route_prefix
        route_prefix.Element = AAZStrArg()

        match_criteria = cls._args_schema.match_criteria
        match_criteria.Element = AAZObjectArg()

        _element = cls._args_schema.match_criteria.Element
        _element.as_path = AAZListArg(
            options=["as-path"],
            help="List of AS paths which this criteria matches.",
        )
        _element.community = AAZListArg(
            options=["community"],
            help="List of BGP communities which this criteria matches.",
        )
        _element.match_condition = AAZStrArg(
            options=["match-condition"],
            help="Match condition to apply RouteMap rules.",
            enum={"Contains": "Contains", "Equals": "Equals", "NotContains": "NotContains", "NotEquals": "NotEquals", "Unknown": "Unknown"},
        )
        _element.route_prefix = AAZListArg(
            options=["route-prefix"],
            help="List of route prefixes which this criteria matches.",
        )

        as_path = cls._args_schema.match_criteria.Element.as_path
        as_path.Element = AAZStrArg()

        community = cls._args_schema.match_criteria.Element.community
        community.Element = AAZStrArg()

        route_prefix = cls._args_schema.match_criteria.Element.route_prefix
        route_prefix.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RouteMapsGet(ctx=self.ctx)()
        self.pre_instance_create()
        self.InstanceCreateByJson(ctx=self.ctx)()
        self.post_instance_create(self.ctx.selectors.subresource.required())
        yield self.RouteMapsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_create(self):
        pass

    @register_callback
    def post_instance_create(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.rules
            filters = enumerate(result)
            filters = filter(
                lambda e: e[0] == self.ctx.args.rule_index,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.rules
            filters = enumerate(result)
            filters = filter(
                lambda e: e[0] == self.ctx.args.rule_index,
                filters
            )
            idx = next(filters, [len(result)])[0]
            self.ctx.args.rule_index = idx
            result[idx] = value
            return

    class RouteMapsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeMaps/{routeMapName}",
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
                    "routeMapName", self.ctx.args.route_map_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualHubName", self.ctx.args.vhub_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
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
            _AddHelper._build_schema_route_map_read(cls._schema_on_200)

            return cls._schema_on_200

    class RouteMapsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeMaps/{routeMapName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                    "routeMapName", self.ctx.args.route_map_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualHubName", self.ctx.args.vhub_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _AddHelper._build_schema_route_map_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._create_instance())

        def _create_instance(self):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType
            )
            _builder.set_prop("actions", AAZListType, ".actions")
            _builder.set_prop("matchCriteria", AAZListType, ".match_criteria")
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("nextStepIfMatched", AAZStrType, ".next_step")

            actions = _builder.get(".actions")
            if actions is not None:
                actions.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".actions[]")
            if _elements is not None:
                _elements.set_prop("parameters", AAZListType, ".parameters")
                _elements.set_prop("type", AAZStrType, ".type")

            parameters = _builder.get(".actions[].parameters")
            if parameters is not None:
                parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".actions[].parameters[]")
            if _elements is not None:
                _elements.set_prop("asPath", AAZListType, ".as_path")
                _elements.set_prop("community", AAZListType, ".community")
                _elements.set_prop("routePrefix", AAZListType, ".route_prefix")

            as_path = _builder.get(".actions[].parameters[].asPath")
            if as_path is not None:
                as_path.set_elements(AAZStrType, ".")

            community = _builder.get(".actions[].parameters[].community")
            if community is not None:
                community.set_elements(AAZStrType, ".")

            route_prefix = _builder.get(".actions[].parameters[].routePrefix")
            if route_prefix is not None:
                route_prefix.set_elements(AAZStrType, ".")

            match_criteria = _builder.get(".matchCriteria")
            if match_criteria is not None:
                match_criteria.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".matchCriteria[]")
            if _elements is not None:
                _elements.set_prop("asPath", AAZListType, ".as_path")
                _elements.set_prop("community", AAZListType, ".community")
                _elements.set_prop("matchCondition", AAZStrType, ".match_condition")
                _elements.set_prop("routePrefix", AAZListType, ".route_prefix")

            as_path = _builder.get(".matchCriteria[].asPath")
            if as_path is not None:
                as_path.set_elements(AAZStrType, ".")

            community = _builder.get(".matchCriteria[].community")
            if community is not None:
                community.set_elements(AAZStrType, ".")

            route_prefix = _builder.get(".matchCriteria[].routePrefix")
            if route_prefix is not None:
                route_prefix.set_elements(AAZStrType, ".")

            return _instance_value


class _AddHelper:
    """Helper class for Add"""

    _schema_route_map_read = None

    @classmethod
    def _build_schema_route_map_read(cls, _schema):
        if cls._schema_route_map_read is not None:
            _schema.etag = cls._schema_route_map_read.etag
            _schema.id = cls._schema_route_map_read.id
            _schema.name = cls._schema_route_map_read.name
            _schema.properties = cls._schema_route_map_read.properties
            _schema.type = cls._schema_route_map_read.type
            return

        cls._schema_route_map_read = _schema_route_map_read = AAZObjectType()

        route_map_read = _schema_route_map_read
        route_map_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        route_map_read.id = AAZStrType(
            flags={"read_only": True},
        )
        route_map_read.name = AAZStrType(
            flags={"read_only": True},
        )
        route_map_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        route_map_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_route_map_read.properties
        properties.associated_inbound_connections = AAZListType(
            serialized_name="associatedInboundConnections",
        )
        properties.associated_outbound_connections = AAZListType(
            serialized_name="associatedOutboundConnections",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rules = AAZListType()

        associated_inbound_connections = _schema_route_map_read.properties.associated_inbound_connections
        associated_inbound_connections.Element = AAZStrType()

        associated_outbound_connections = _schema_route_map_read.properties.associated_outbound_connections
        associated_outbound_connections.Element = AAZStrType()

        rules = _schema_route_map_read.properties.rules
        rules.Element = AAZObjectType()

        _element = _schema_route_map_read.properties.rules.Element
        _element.actions = AAZListType()
        _element.match_criteria = AAZListType(
            serialized_name="matchCriteria",
        )
        _element.name = AAZStrType()
        _element.next_step_if_matched = AAZStrType(
            serialized_name="nextStepIfMatched",
        )

        actions = _schema_route_map_read.properties.rules.Element.actions
        actions.Element = AAZObjectType()

        _element = _schema_route_map_read.properties.rules.Element.actions.Element
        _element.parameters = AAZListType()
        _element.type = AAZStrType()

        parameters = _schema_route_map_read.properties.rules.Element.actions.Element.parameters
        parameters.Element = AAZObjectType()

        _element = _schema_route_map_read.properties.rules.Element.actions.Element.parameters.Element
        _element.as_path = AAZListType(
            serialized_name="asPath",
        )
        _element.community = AAZListType()
        _element.route_prefix = AAZListType(
            serialized_name="routePrefix",
        )

        as_path = _schema_route_map_read.properties.rules.Element.actions.Element.parameters.Element.as_path
        as_path.Element = AAZStrType()

        community = _schema_route_map_read.properties.rules.Element.actions.Element.parameters.Element.community
        community.Element = AAZStrType()

        route_prefix = _schema_route_map_read.properties.rules.Element.actions.Element.parameters.Element.route_prefix
        route_prefix.Element = AAZStrType()

        match_criteria = _schema_route_map_read.properties.rules.Element.match_criteria
        match_criteria.Element = AAZObjectType()

        _element = _schema_route_map_read.properties.rules.Element.match_criteria.Element
        _element.as_path = AAZListType(
            serialized_name="asPath",
        )
        _element.community = AAZListType()
        _element.match_condition = AAZStrType(
            serialized_name="matchCondition",
        )
        _element.route_prefix = AAZListType(
            serialized_name="routePrefix",
        )

        as_path = _schema_route_map_read.properties.rules.Element.match_criteria.Element.as_path
        as_path.Element = AAZStrType()

        community = _schema_route_map_read.properties.rules.Element.match_criteria.Element.community
        community.Element = AAZStrType()

        route_prefix = _schema_route_map_read.properties.rules.Element.match_criteria.Element.route_prefix
        route_prefix.Element = AAZStrType()

        _schema.etag = cls._schema_route_map_read.etag
        _schema.id = cls._schema_route_map_read.id
        _schema.name = cls._schema_route_map_read.name
        _schema.properties = cls._schema_route_map_read.properties
        _schema.type = cls._schema_route_map_read.type


__all__ = ["Add"]
