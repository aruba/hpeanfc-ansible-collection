#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_discovery
version_added: "0.0.1"
short_description: Run discovery of the switches matching the IP addresses.
description: >
    This module discovers the switches matching the input IP addresses.
options:
    afc_ip:
        description: >
            IP address of the HPE ANW Fabric Composer.
        type: str
        required: true
    afc_username:
        description:
        - User account having write permission on the HPE ANW Fabric Composer
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
    data:
        description: >
            List of IP addresses of the devices that need to be discovered,
            with credentials required for discovery.
        type: dict
        required: true
        suboptions:
            switches:
                description: List of IP Addresses or ranges to discover
                type: list
                elements: str
                required: true
            admin_passwd:
                description: Admin password to connect on switches.
                type: str
                required: true
            afc_admin_passwd:
                description: AFC user password to be created on switches
                type: str
                required: true
            service_account_user:
                description: >
                    AFC user to be created on switches.
                type: str
                default: admin
                required: false

author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Run discovery of the switches through AFC using username and password
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"

-   name: Run discovery of the switches through AFC using username and password
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11-10.10.10.20"
                - "10.10.10.22"

-   name: Run discovery of the switches through AFC using token
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
"""

RETURN = r"""
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
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arubanetworks.afc.plugins.module_utils.afc import (
    instantiate_afc_object,
)
from pyafc.switches import switches


def main():
    module_args = {
        "afc_ip": {"type": "str", "required": True},
        "afc_username": {"type": "str", "required": False},
        "afc_password": {"type": "str", "required": False},
        "auth_token": {"type": "str", "required": False},
        "data": {"type": "dict", "required": True},
    }

    ansible_module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    # Get playbook's arguments
    token = None
    ip = ansible_module.params["afc_ip"]
    if "afc_username" in list(ansible_module.params.keys()):
        username = ansible_module.params["afc_username"]
    if "afc_password" in list(ansible_module.params.keys()):
        password = ansible_module.params["afc_password"]
    if "auth_token" in list(ansible_module.params.keys()):
        token = ansible_module.params["auth_token"]
    data = ansible_module.params["data"]

    if token is not None:
        auth_data = {"ip": ip, "auth_token": token}
    else:
        auth_data = {"ip": ip, "username": username, "password": password}

    result = {"changed": False}

    if ansible_module.check_mode:
        ansible_module.exit_json(**result)

    status = False
    changed = False
    message = ""

    afc_instance = instantiate_afc_object(data=auth_data)

    if afc_instance.afc_connected:
        switches_instance = switches.Switch(
            afc_instance.client,
        )
        message, status, changed = switches_instance.discover_multiple_devices(
            **data,
        )
        # Disconnect session if username and password are passed
        if username and password:
            afc_instance.disconnect()
    else:
        message = "Not connected to AFC"

    result["message"] = message
    result["status"] = status
    result["changed"] = changed

    # Exit
    if status:
        ansible_module.exit_json(changed=changed, msg=message)
    else:
        ansible_module.fail_json(changed=changed, msg=message)


if __name__ == "__main__":
    main()
