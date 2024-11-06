#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright 2019-2023 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: afc_dss
version_added: "0.0.1"
short_description: Create or delete a DSS configuration.
description: >
    This module creates or deletes a DSS configuration.
options:
    afc_ip:
        description: >
            IP address of the Aruba Fabric Composer.
        type: str
        required: true
    afc_username:
        description:
        - User account having permission to create VRF on the Aruba Fabric Composer
        type: str
        required: false
    afc_password:
        description:
        - Password of the user account
        type: str
        required: false
    auth_token:
        description: >
            Auth token from the create session playbook.
        type: str
        required: false
    dss_object_name:
        description: >
            Name of the object that will be created or deleted from.
        type: str
        required: true
    dss_object_type:
        description: >
            Type of the dss object. Options policy, endpoint_group, rule, qualifier, vnic_move.
        type: str
        required: true
    dss_object_data:
        description: >
            Object specific data for policy, endpoint_group, rule, qualifier, vnic_move.
        type: dict
        required: true
    operation:
        description: >
            Operation to be performed on the DSS configuration, create or delete.
        type: str
        required: true
author: Aruba Networks (@ArubaNetworks)
'''

EXAMPLES = r'''
-   name: Create policy
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        dss_object_data:
            policy_subtype: "firewall"
            priority: 10
            rules:
                - "test_rule"
            enforcers:
                -   fabric: "Test-Fabric"
                    vrf: "Test-VRF"
                    network: "VLAN251"
                    enforcer_type: "network"
                    direction: "egress"
                    pdt_type: "leaf"
            object_type: "policy"
        operation: "create"

-   name: Delete policy
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        operation: "delete"

-   name: Create rule
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        dss_object_data:
            action: "drop"
            source_endpoint_groups:
                - "test_eg"
            destination_endpoint_groups:
                - "test_eg"
            service_qualifiers:
                - "icmp"
                - "bgp"
                - "test_sq"
        operation: "create"

-   name: Delete rule
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        operation: "delete"

-   name: Create endpoint group
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        dss_object_data:
            type: "layer3"
            endpoints:
                -   vm_name: "Test-Fabric"
                    vnic_name: "Network adapter 1"
        operation: "create"

-   name: Delete endpoint group
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        operation: "delete"

-   name: Create qualifier
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        dss_object_data:
            protocol_identifier:
                -   src_port: "32"
                    dst_port: "32"
                    ip_protocol: "tcp"
            qualifier_type: "layer3"
        operation: "create"

-   name: Delete qualifier
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        operation: "delete"
'''


RETURN = r'''
message:
    description: The output generated by the module
    type: str
    returned: always
    sample: "Successfully completed configuration"
status:
    description: True or False depending on the action taken
    type: bool
    returned: always
    sample: True
changed:
    description: True or False if something has been changed or not
    type: bool
    returned: always
    sample: True
'''

from pyafc.dss import policies
from pyafc.dss import endpoint_groups
from pyafc.dss import qualifiers
from pyafc.dss import rules

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arubanetworks.afc.plugins.module_utils.afc import instantiate_afc_object


def main():
    module_args = dict(
        afc_ip=dict(type="str", required=True),
        afc_username=dict(type="str", required=False),
        afc_password=dict(type="str", required=False),
        auth_token=dict(type="str", required=False),
        dss_object_name=dict(type="str", required=True),
        dss_object_type=dict(type="str", required=True),
        dss_object_data=dict(type="dict", required=False),
        operation=dict(type="str", required=True),
    )

    ansible_module = AnsibleModule(
        argument_spec=module_args, supports_check_mode=True
    )

    # Get playbook's arguments
    token = None
    ip = ansible_module.params["afc_ip"]
    if 'afc_username' in list(ansible_module.params.keys()):
        username = ansible_module.params["afc_username"]
    if 'afc_password' in list(ansible_module.params.keys()):
        password = ansible_module.params["afc_password"]
    if 'auth_token' in list(ansible_module.params.keys()):
        token = ansible_module.params["auth_token"]
    dss_object_name = ansible_module.params["dss_object_name"]
    dss_object_type = ansible_module.params["dss_object_type"]
    operation = ansible_module.params["operation"]
    if 'dss_object_data' in list(ansible_module.params.keys()):
        dss_object_data = ansible_module.params["dss_object_data"]

    if token is not None:
        data = {
            "ip": ip,
            "auth_token": token
        }
    else:
        data = {
            "ip": ip,
            "username": username,
            "password": password
        }

    afc_instance = instantiate_afc_object(data=data)

    result = dict(changed=False)

    if ansible_module.check_mode:
        ansible_module.exit_json(**result)

    status = False
    changed = False
    message = ""

    if operation == 'create':
        if dss_object_type == 'policy':
            policy_instance = policies.Policy(afc_instance.client, name=dss_object_name)
            message, status, changed = policy_instance.create_policy(**dss_object_data)
        elif dss_object_type == 'rule':
            rule_instance = rules.Rule(afc_instance.client, name=dss_object_name)
            message, status, changed = rule_instance.create_rule(**dss_object_data)
        elif dss_object_type == 'endpoint_group':
            eg_instance = endpoint_groups.EndpointGroup(afc_instance.client, name=dss_object_name)
            message, status, changed = eg_instance.create_eg(**dss_object_data)
        elif dss_object_type == 'qualifier':
            qualifier_instance = qualifiers.Qualifier(afc_instance.client, name=dss_object_name)
            message, status, changed = qualifier_instance.create_qualifier(**dss_object_data)

    elif operation == 'delete':
        if dss_object_type == 'policy':
            policy_instance = policies.Policy(afc_instance.client, name=dss_object_name)
            message, status, changed = policy_instance.delete_policy()
        elif dss_object_type == 'rule':
            rule_instance = rules.Rule(afc_instance.client, name=dss_object_name)
            message, status, changed = rule_instance.delete_rule()
        elif dss_object_type == 'endpoint_group':
            eg_instance = endpoint_groups.EndpointGroup(afc_instance.client, name=dss_object_name)
            message, status, changed = eg_instance.delete_eg()
        elif dss_object_type == 'qualifier':
            qualifier_instance = qualifiers.Qualifier(afc_instance.client, name=dss_object_name)
            message, status, changed = qualifier_instance.delete_qualifier()

    result['message'] = message
    result['status'] = status
    result['changed'] = changed

    # Disconnect session if username and password are passed
    if username and password:
        afc_instance.disconnect()

    # Exit
    if status:
        ansible_module.exit_json(changed=changed, msg=message)
    else:
        ansible_module.fail_json(changed=changed, msg=message)


if __name__ == "__main__":
    main()
