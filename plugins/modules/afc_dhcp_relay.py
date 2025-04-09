#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_dhcp_relay
version_added: "0.0.1"
short_description: Create or delete DHCP Relay configuration in the fabric.
description: >
    This module creates or deletes a DHCP Relay configuration in the fabric.
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
    operation:
        description: >
            Operation to be performed on the DHCP Relay configuration,
            create or delete.
        type: str
        choices:
            - create
            - delete
        required: true
    data:
        description: >
            Dictionary containing mandatory details to create a DHCP relay.
            Required for create and not required for delete.
            Structure is provided in the example.
        type: dict
        required: true
        suboptions:
            name:
                description: DHCP Relay Config name
                type: str
                required: true
            description:
                description: DHCP Relay Config description
                type: str
                required: false
            vlans:
                description: Set or range of VLANs
                type: str
                required: false
            gateway_address:
                description: BOOTP-Gateway Address
                type: str
                required: false
            ipv4_dhcp_server_addresses:
                description: List of DHCP Servers IPv4 Addresses
                type: list
                elements: str
                required: false
            ipv6_dhcp_server_addresses:
                description: List of DHCP Servers IPv6 Addresses
                type: list
                elements: str
                required: false
            ipv6_dhcp_mcast_server_addresses:
                description: List of DHCP Servers IPv6 MCAST Addresses
                type: list
                elements: str
                required: false
            v4relay_option82_policy:
                description: >
                    Specifies the forwarding policy of DHCP-Relay Option 82
                type: str
                choices:
                    - replace
                    - drop
                    - keep
                required: false
            v4relay_option82_validation:
                description: >
                    Set true to validate server response packets and set it
                    to false otherwise.
                    This configuration is disabled by default
                type: bool
                required: false
            v4relay_source_interface:
                description: >
                    Set true to enable DHCP-Relay to use the configured
                    source-interface and include suboption-5 and
                    suboption-11 in the relay option 82.
                    This configuration is disabled by default
                type: bool
                required: false
            fabrics:
                description: List of Fabrics
                type: list
                elements: str
                required: false
            switches:
                description: List of Switches
                type: list
                elements: str
                required: false

author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Create DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-DHCP_Relay"
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        name: "Test-DHCP_Relay"
        operation: "delete"

-   name: Create DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-DHCP_Relay"
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        name: "Test-DHCP_Relay"
        operation: "delete"
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
from pyafc.services import dhcp_relay


def main():
    module_args = {
        "afc_ip": {"type": "str", "required": True},
        "afc_username": {"type": "str", "required": False},
        "afc_password": {"type": "str", "required": False},
        "auth_token": {"type": "str", "required": False},
        "operation": {"type": "str", "required": True},
        "data": {"type": "dict", "required": False},
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
    operation = ansible_module.params["operation"]
    data = ansible_module.params["data"]

    if token is not None:
        auth_data = {
            "ip": ip,
            "auth_token": token,
        }
    else:
        auth_data = {
            "ip": ip,
            "username": username,
            "password": password,
        }

    result = {"changed": False}

    if ansible_module.check_mode:
        ansible_module.exit_json(**result)

    status = False
    changed = False
    message = ""

    afc_instance = instantiate_afc_object(data=auth_data)

    if afc_instance.afc_connected:

        if operation == "create":
            dhcp_relay_instance = dhcp_relay.DhcpRelay(
                afc_instance.client,
                **data,
            )
            message, status, changed = dhcp_relay_instance.create_dhcp_relay(
                **data,
            )
        elif operation == "delete":
            dhcp_relay_instance = dhcp_relay.DhcpRelay(
                afc_instance.client,
                name=data["name"],
            )
            if dhcp_relay_instance.uuid:
                message, status, changed = (
                    dhcp_relay_instance.delete_dhcp_relay()
                )
            else:
                message = "DHCP Relay does not exist - No action taken"
        else:
            message = "Operation not supported - No action taken"

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
