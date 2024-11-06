#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright 2019-2023 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: afc_ntp
version_added: "0.0.1"
short_description: Create or delete a NTP configuration in the specified fabric.
description: >
    This module creates or deletes a NTP configuration in the specified fabric.
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
    operation:
        description: >
            Operation to be performed on the NTP configuration, create or delete.
        type: str
        required: true
    ntp_name:
        description: >
            Name of the NTP Entry.
        type: str
        required: true
    ntp_data:
        description: >
            Data of NTP configuration as depicted in the example. Required for create operation and not required for delete.
        type: dict
        required: false
author: Aruba Networks (@ArubaNetworks)
'''

EXAMPLES = r'''
-   name: Create NTP configuration
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        ntp_name: "Test-NTP"
        operation: "create"
        ntp_data:
            fabrics:
                - "Test-Fabric"
            servers:
                -   server: "10.100.100.111"
                    burst_mode: "iburst"
                    prefer: True

-   name: Delete NTP configuration
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        ntp_name: "Test-NTP"
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

from pyafc.services import ntp
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arubanetworks.afc.plugins.module_utils.afc import instantiate_afc_object


def main():
    module_args = dict(
        afc_ip=dict(type="str", required=True),
        afc_username=dict(type="str", required=False),
        afc_password=dict(type="str", required=False),
        auth_token=dict(type="str", required=False),
        operation=dict(type="str", required=True),
        ntp_name=dict(type="str", required=True),
        ntp_data=dict(type="dict", required=False)
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
    ntp_name = ansible_module.params["ntp_name"]
    operation = ansible_module.params["operation"]
    if 'ntp_data' in list(ansible_module.params.keys()):
        ntp_data = ansible_module.params["ntp_data"]

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
        ntp_instance = ntp.Ntp(afc_instance.client, name=ntp_name, **ntp_data)
        message, status, changed = ntp_instance.create_ntp(**ntp_data)
    elif operation == 'delete':
        ntp_instance = ntp.Ntp(afc_instance.client, name=ntp_name)
        message, status, changed = ntp_instance.delete_ntp()

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
