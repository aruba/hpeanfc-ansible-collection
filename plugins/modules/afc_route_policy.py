#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright 2019-2023 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: afc_route_policy
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
    rp_object_name:
        description: >
            Name of the route policy object that will be created or deleted from.
        type: str
        required: true
    rp_object_type:
        description: >
            Type of the route policy object. Options route_map, prefix_list, community_list, aspath_list.
        type: str
        required: true
    rp_object_data:
        description: >
            Object specific data for route_map, prefix_list, community_list, aspath_list.
        type: dict
        required: true
    operation:
        description: >
            Operation to be performed on the Route Policy configuration, create or delete.
        type: str
        required: true
author: Aruba Networks (@ArubaNetworks)
'''

EXAMPLES = r'''
-   name: Create Route Map
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        rp_object_data:
            switches: '10.10.10.109'
            entries:
            -   seq: 10
                action: "deny"
                description: "ee"
                route_map_continue: 20
                match_vni: 10100
                set_origin: "igp"
            -   seq: 20
                action: "deny"
                match_tag: 100
        operation: "create"

-   name: Delete Route Map
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        operation: "delete"

-   name: Create ASPath List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        rp_object_data:
            switches: '10.10.10.109'
            entries:
            -   description: ""
                seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Delete ASPath List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        operation: "delete"

-   name: Create Community List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        rp_object_data:
            switches: '10.10.10.11'
            type: "community-expanded-list"
            entries:
            -   description: ""
                seq: 10
                action: "deny"
                match_string: "internet"
        operation: "create"

-   name: Delete Community List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        operation: "delete"

-   name: Create Prefix List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
        rp_object_data:
            seq: 20
            action: "permit"
            prefix:
                address: "10.10.20.0"
                prefix_length: 24
        operation: "create"

-   name: Delete Prefix List
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
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

from pyafc.route_policies import route_maps
from pyafc.route_policies import community_lists
from pyafc.route_policies import prefix_lists
from pyafc.route_policies import as_path_lists

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arubanetworks.afc.plugins.module_utils.afc import instantiate_afc_object


def main():
    module_args = dict(
        afc_ip=dict(type="str", required=True),
        afc_username=dict(type="str", required=False),
        afc_password=dict(type="str", required=False),
        auth_token=dict(type="str", required=False),
        rp_object_name=dict(type="str", required=True),
        rp_object_type=dict(type="str", required=True),
        rp_object_data=dict(type="dict", required=False),
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
    rp_object_name = ansible_module.params["rp_object_name"]
    rp_object_type = ansible_module.params["rp_object_type"]
    operation = ansible_module.params["operation"]
    if 'rp_object_data' in list(ansible_module.params.keys()):
        rp_object_data = ansible_module.params["rp_object_data"]

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
        if rp_object_type == 'route_map':
            route_map_instance = route_maps.RouteMap(afc_instance.client, name=rp_object_name)
            message, status, changed = route_map_instance.create_routemap(**rp_object_data)
        elif rp_object_type == 'aspath_list':
            aspath_list_instance = as_path_lists.ASPathList(afc_instance.client, name=rp_object_name)
            message, status, changed = aspath_list_instance.create_aspath_list(**rp_object_data)
        elif rp_object_type == 'prefix_list':
            prefix_list_instance = prefix_lists.PrefixList(afc_instance.client, name=rp_object_name)
            message, status, changed = prefix_list_instance.create_prefix_list(**rp_object_data)
        elif rp_object_type == 'community_list':
            community_list_instance = community_lists.CommunityList(afc_instance.client, name=rp_object_name)
            message, status, changed = community_list_instance.create_community_list(**rp_object_data)

    elif operation == 'delete':
        if rp_object_type == 'route_map':
            route_map_instance = route_maps.RouteMap(afc_instance.client, name=rp_object_name)
            message, status, changed = route_map_instance.delete_routemap()
        elif rp_object_type == 'aspath_list':
            aspath_list_instance = as_path_lists.ASPathList(afc_instance.client, name=rp_object_name)
            message, status, changed = aspath_list_instance.delete_aspath_list()
        elif rp_object_type == 'prefix_list':
            prefix_list_instance = prefix_lists.PrefixList(afc_instance.client, name=rp_object_name)
            message, status, changed = prefix_list_instance.delete_prefix_list()
        elif rp_object_type == 'community_list':
            community_list_instance = community_lists.CommunityList(afc_instance.client, name=rp_object_name)
            message, status, changed = community_list_instance.delete_community_list()

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
