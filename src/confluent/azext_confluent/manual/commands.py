# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=import-outside-toplevel

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_confluent.generated._client_factory import cf_organization

    confluent_organization = CliCommandType(
        operations_tmpl='azext_confluent.vendored_sdks.confluent.operations._organization_operations#OrganizationOperat'
        'ions.{}',
        client_factory=cf_organization)
    with self.command_group('confluent organization', confluent_organization, client_factory=cf_organization) as g:
        g.custom_command('delete', 'confluent_organization_delete', supports_no_wait=True)

    with self.command_group('confluent offer-detail') as g:
        g.custom_show_command('show', 'confluent_offer_detail_show')

    from azext_confluent.generated._client_factory import cf_marketplace_agreement

    confluent_marketplace_agreement = CliCommandType(
        operations_tmpl='azext_confluent.vendored_sdks.confluent.operations._marketplace_agreements_operations#Marketpl'
        'aceAgreementsOperations.{}',
        client_factory=cf_marketplace_agreement)
    with self.command_group('confluent terms', confluent_marketplace_agreement,
                            client_factory=cf_marketplace_agreement,
                            deprecate_info=g.deprecate(redirect='az term', hide=True)) as g:
        g.custom_command('list', 'confluent_terms_list')
