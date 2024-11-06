#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright 2019-2023 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: afc_ospf
version_added: "0.0.1"
short_description: Create or delete an OSPF configuration.
description: >
    This module creates or deletes an OSPF configuration.
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
    fabric_name:
        description: >
            Name of the Fabric.
        type: str
        required: true
    vrf_name:
        description: >
            Name of the VRF in which OSPF objects are to be created or deleted from.
        type: str
        required: true
    ospf_object_name:
        description: >
            Name of the OSPF object object that will be created or deleted from.
        type: str
        required: true
    ospf_object_type:
        description: >
            Type of the OSPF Object object. Options router, area, interface.
        type: str
        required: true
    ospf_object_data:
        description: >
            Object specific data for OSPF router or area or interface.
        type: dict
        required: true
    operation:
        description: >
            Operation to be performed on the OSPF object, create or delete.
        type: str
        required: true
author: Aruba Networks (@ArubaNetworks)
'''

EXAMPLES = r'''
-   name: Create OSPF Router
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        ospf_object_data:
            instance: "Test-OSPF-Router"
            switches: "10.1.66.11"
            id: 10
            redistribute:
                redistribute_bgp: false
        operation: "create"

-   name: Delete OSPF Router
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        operation: "delete"

-   name: Create OSPF Area
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        ospf_object_data:
            ospf_router: "Test-OSPF-Router"
            switches: "10.1.66.11"
        operation: "create"

-   name: Delete OSPF Area
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        operation: "delete"

-   name: Create OSPF Interface
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
        ospf_object_data:
            router: "10.10.10.254"
            area: "0.0.0.1"
            interface: "1/1/29"
            network_type: "ospf_iftype_pointopoint"
        operation: "create"

-   name: Delete OSPF Interface
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
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

from pyafc.fabric import fabric
from pyafc.vrf import vrf

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arubanetworks.afc.plugins.module_utils.afc import instantiate_afc_object


def main():
    module_args = dict(
        afc_ip=dict(type="str", required=True),
        afc_username=dict(type="str", required=False),
        afc_password=dict(type="str", required=False),
        auth_token=dict(type="str", required=False),
        fabric_name=dict(type="str", required=True),
        vrf_name=dict(type="str", required=True),
        ospf_object_name=dict(type="str", required=True),
        ospf_object_type=dict(type="str", required=True),
        ospf_object_data=dict(type="dict", required=False),
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
    fabric_name = ansible_module.params["fabric_name"]
    vrf_name = ansible_module.params["vrf_name"]
    ospf_object_name = ansible_module.params["ospf_object_name"]
    ospf_object_type = ansible_module.params["ospf_object_type"]
    operation = ansible_module.params["operation"]
    if 'ospf_object_data' in list(ansible_module.params.keys()):
        ospf_object_data = ansible_module.params["ospf_object_data"]

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
    fabric_instance = fabric.Fabric(afc_instance.client, name=fabric_name)
    vrf_instance = vrf.Vrf(afc_instance.client, name=vrf_name, fabric_uuid=fabric_instance.uuid)

    result = dict(changed=False)

    if ansible_module.check_mode:
        ansible_module.exit_json(**result)

    status = False
    changed = False
    message = ""

    if operation == 'create':
        if ospf_object_type == 'router':
            message, status, changed = vrf_instance.create_ospf_router(name=ospf_object_name, **ospf_object_data)
        elif ospf_object_type == 'area':
            message, status, changed = vrf_instance.create_ospf_area(name=ospf_object_name, **ospf_object_data)
        elif ospf_object_type == 'interface':
            message, status, changed = vrf_instance.create_ospf_interface(name=ospf_object_name, **ospf_object_data)

    elif operation == 'delete':
        if ospf_object_type == 'router':
            message, status, changed = vrf_instance.delete_ospf_router(name=ospf_object_name)
        elif ospf_object_type == 'area':
            message, status, changed = vrf_instance.delete_ospf_area(name=ospf_object_name)
        elif ospf_object_type == 'interface':
            message, status, changed = vrf_instance.delete_ospf_interface(name=ospf_object_name)

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
