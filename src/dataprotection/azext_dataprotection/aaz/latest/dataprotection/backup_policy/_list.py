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
    "dataprotection backup-policy list",
    is_experimental=True,
)
class List(AAZCommand):
    """List list of backup policies belonging to a backup vault

    :example: List Backup Policies
        az dataprotection backup-policy list --resource-group "000pikumar" --vault-name "PrivatePreviewVault"
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults/{}/backuppolicies", "2023-11-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["-v", "--vault-name"],
            help="The name of the backup vault.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BackupPoliciesList(ctx=self.ctx)()
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

    class BackupPoliciesList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}/backupPolicies",
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
                **self.serialize_url_param(
                    "vaultName", self.ctx.args.vault_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
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
            _element.properties = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.datasource_types = AAZListType(
                serialized_name="datasourceTypes",
                flags={"required": True},
            )
            properties.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            datasource_types = cls._schema_on_200.value.Element.properties.datasource_types
            datasource_types.Element = AAZStrType()

            disc_backup_policy = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy")
            disc_backup_policy.policy_rules = AAZListType(
                serialized_name="policyRules",
                flags={"required": True},
            )

            policy_rules = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules
            policy_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            disc_azure_backup_rule = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule")
            disc_azure_backup_rule.backup_parameters = AAZObjectType(
                serialized_name="backupParameters",
            )
            disc_azure_backup_rule.data_store = AAZObjectType(
                serialized_name="dataStore",
                flags={"required": True},
            )
            _ListHelper._build_schema_data_store_info_base_read(disc_azure_backup_rule.data_store)
            disc_azure_backup_rule.trigger = AAZObjectType(
                flags={"required": True},
            )

            backup_parameters = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").backup_parameters
            backup_parameters.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            disc_azure_backup_params = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").backup_parameters.discriminate_by("object_type", "AzureBackupParams")
            disc_azure_backup_params.backup_type = AAZStrType(
                serialized_name="backupType",
                flags={"required": True},
            )

            trigger = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger
            trigger.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            disc_adhoc_based_trigger_context = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "AdhocBasedTriggerContext")
            disc_adhoc_based_trigger_context.tagging_criteria = AAZObjectType(
                serialized_name="taggingCriteria",
                flags={"required": True},
            )

            tagging_criteria = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "AdhocBasedTriggerContext").tagging_criteria
            tagging_criteria.tag_info = AAZObjectType(
                serialized_name="tagInfo",
            )
            _ListHelper._build_schema_retention_tag_read(tagging_criteria.tag_info)

            disc_schedule_based_trigger_context = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext")
            disc_schedule_based_trigger_context.schedule = AAZObjectType(
                flags={"required": True},
            )
            disc_schedule_based_trigger_context.tagging_criteria = AAZListType(
                serialized_name="taggingCriteria",
                flags={"required": True},
            )

            schedule = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").schedule
            schedule.repeating_time_intervals = AAZListType(
                serialized_name="repeatingTimeIntervals",
                flags={"required": True},
            )
            schedule.time_zone = AAZStrType(
                serialized_name="timeZone",
            )

            repeating_time_intervals = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").schedule.repeating_time_intervals
            repeating_time_intervals.Element = AAZStrType()

            tagging_criteria = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria
            tagging_criteria.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element
            _element.criteria = AAZListType()
            _element.is_default = AAZBoolType(
                serialized_name="isDefault",
                flags={"required": True},
            )
            _element.tag_info = AAZObjectType(
                serialized_name="tagInfo",
                flags={"required": True},
            )
            _ListHelper._build_schema_retention_tag_read(_element.tag_info)
            _element.tagging_priority = AAZIntType(
                serialized_name="taggingPriority",
                flags={"required": True},
            )

            criteria = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria
            criteria.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element
            _element.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            disc_schedule_based_backup_criteria = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria")
            disc_schedule_based_backup_criteria.absolute_criteria = AAZListType(
                serialized_name="absoluteCriteria",
            )
            disc_schedule_based_backup_criteria.days_of_month = AAZListType(
                serialized_name="daysOfMonth",
            )
            disc_schedule_based_backup_criteria.days_of_the_week = AAZListType(
                serialized_name="daysOfTheWeek",
            )
            disc_schedule_based_backup_criteria.months_of_year = AAZListType(
                serialized_name="monthsOfYear",
            )
            disc_schedule_based_backup_criteria.schedule_times = AAZListType(
                serialized_name="scheduleTimes",
            )
            disc_schedule_based_backup_criteria.weeks_of_the_month = AAZListType(
                serialized_name="weeksOfTheMonth",
            )

            absolute_criteria = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").absolute_criteria
            absolute_criteria.Element = AAZStrType()

            days_of_month = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").days_of_month
            days_of_month.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").days_of_month.Element
            _element.date = AAZIntType()
            _element.is_last = AAZBoolType(
                serialized_name="isLast",
            )

            days_of_the_week = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").days_of_the_week
            days_of_the_week.Element = AAZStrType()

            months_of_year = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").months_of_year
            months_of_year.Element = AAZStrType()

            schedule_times = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").schedule_times
            schedule_times.Element = AAZStrType()

            weeks_of_the_month = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureBackupRule").trigger.discriminate_by("object_type", "ScheduleBasedTriggerContext").tagging_criteria.Element.criteria.Element.discriminate_by("object_type", "ScheduleBasedBackupCriteria").weeks_of_the_month
            weeks_of_the_month.Element = AAZStrType()

            disc_azure_retention_rule = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule")
            disc_azure_retention_rule.is_default = AAZBoolType(
                serialized_name="isDefault",
            )
            disc_azure_retention_rule.lifecycles = AAZListType(
                flags={"required": True},
            )

            lifecycles = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles
            lifecycles.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element
            _element.delete_after = AAZObjectType(
                serialized_name="deleteAfter",
                flags={"required": True},
            )
            _element.source_data_store = AAZObjectType(
                serialized_name="sourceDataStore",
                flags={"required": True},
            )
            _ListHelper._build_schema_data_store_info_base_read(_element.source_data_store)
            _element.target_data_store_copy_settings = AAZListType(
                serialized_name="targetDataStoreCopySettings",
            )

            delete_after = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element.delete_after
            delete_after.duration = AAZStrType(
                flags={"required": True},
            )
            delete_after.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            target_data_store_copy_settings = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element.target_data_store_copy_settings
            target_data_store_copy_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element.target_data_store_copy_settings.Element
            _element.copy_after = AAZObjectType(
                serialized_name="copyAfter",
                flags={"required": True},
            )
            _element.data_store = AAZObjectType(
                serialized_name="dataStore",
                flags={"required": True},
            )
            _ListHelper._build_schema_data_store_info_base_read(_element.data_store)

            copy_after = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element.target_data_store_copy_settings.Element.copy_after
            copy_after.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            disc_custom_copy_option = cls._schema_on_200.value.Element.properties.discriminate_by("object_type", "BackupPolicy").policy_rules.Element.discriminate_by("object_type", "AzureRetentionRule").lifecycles.Element.target_data_store_copy_settings.Element.copy_after.discriminate_by("object_type", "CustomCopyOption")
            disc_custom_copy_option.duration = AAZStrType()

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

    _schema_data_store_info_base_read = None

    @classmethod
    def _build_schema_data_store_info_base_read(cls, _schema):
        if cls._schema_data_store_info_base_read is not None:
            _schema.data_store_type = cls._schema_data_store_info_base_read.data_store_type
            _schema.object_type = cls._schema_data_store_info_base_read.object_type
            return

        cls._schema_data_store_info_base_read = _schema_data_store_info_base_read = AAZObjectType()

        data_store_info_base_read = _schema_data_store_info_base_read
        data_store_info_base_read.data_store_type = AAZStrType(
            serialized_name="dataStoreType",
            flags={"required": True},
        )
        data_store_info_base_read.object_type = AAZStrType(
            serialized_name="objectType",
            flags={"required": True},
        )

        _schema.data_store_type = cls._schema_data_store_info_base_read.data_store_type
        _schema.object_type = cls._schema_data_store_info_base_read.object_type

    _schema_retention_tag_read = None

    @classmethod
    def _build_schema_retention_tag_read(cls, _schema):
        if cls._schema_retention_tag_read is not None:
            _schema.e_tag = cls._schema_retention_tag_read.e_tag
            _schema.id = cls._schema_retention_tag_read.id
            _schema.tag_name = cls._schema_retention_tag_read.tag_name
            return

        cls._schema_retention_tag_read = _schema_retention_tag_read = AAZObjectType()

        retention_tag_read = _schema_retention_tag_read
        retention_tag_read.e_tag = AAZStrType(
            serialized_name="eTag",
            flags={"read_only": True},
        )
        retention_tag_read.id = AAZStrType(
            flags={"read_only": True},
        )
        retention_tag_read.tag_name = AAZStrType(
            serialized_name="tagName",
            flags={"required": True},
        )

        _schema.e_tag = cls._schema_retention_tag_read.e_tag
        _schema.id = cls._schema_retention_tag_read.id
        _schema.tag_name = cls._schema_retention_tag_read.tag_name


__all__ = ["List"]
