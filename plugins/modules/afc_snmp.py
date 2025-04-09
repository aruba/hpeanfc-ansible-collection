#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_snmp
version_added: "0.0.1"
short_description: Create or delete an SNMP configuration.
description: >
    This module creates or deletes an SNMP configuration.
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
            Operation to be performed on an SNMP configuration,
            create or delete.
        type: str
        choices:
            - create
            - delete
        required: true
    data:
        description: >
            SNMP configuration in dictionary format as depicted in the example.
            Structure is provided in the example.
        type: dict
        suboptions:
            name:
                description: SNMP Workflow Name
                type: str
                required: true
            fabrics:
                description: List of fabrics
                type: list
                elements: str
                required: true
            enable:
                description: Enable configuration
                type: bool
                default: true
                required: false
            location:
                description: SNMP Location
                type: str
                required: false
            contact:
                description: SNMP contact
                type: str
                required: false
            community:
                description: SNMP community
                type: str
                required: false
            agent_port:
                description: SNMP Agent port
                type: int
                default: 161
                required: false
            trap_port:
                description: SNMP Trap port
                type: int
                required: false
            users:
                description: SNMPv3 user
                type: list
                elements: dict
                suboptions:
                    name:
                        description: Username
                        type: str
                        required: true
                    level:
                        description: User level
                        type: str
                        choices:
                            - noauth
                            - auth
                            - priv
                        required: true
                    auth_type:
                        description: User Authentication Type
                        type: str
                        choices:
                            - SHA
                            - MD5
                        default: SHA
                        required: false
                    auth_pass:
                        description: User Authentication Password
                        type: str
                        required: false
                    priv_type:
                        description: User Privacy Type
                        type: str
                        choices:
                            - AES
                            - DES
                        default: AES
                        required: false
                    priv_pass:
                        description: User Privacy Password
                        type: str
                        required: false
                    context:
                        description: SNMPv3 context
                        type: str
                        required: false
                required: false
            servers:
                description: SNMP servers
                type: list
                elements: dict
                suboptions:
                    address:
                        description: Server's IPv4 address
                        type: str
                        required: true
                    community:
                        description: SNMP Community
                        type: str
                        required: true
                required: false
        required: true
author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Create an SNMPv3 configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "snmp_admin"
                    auth_type: "SHA"
                    auth_pass: "password"
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration with Trap Server using username and
          password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Create an SNMPv2c configuration only on some devices using
          username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Delete an SNMP configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-SNMP"
        operation: "delete"

-   name: Create an SNMPv3 configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "snmp_admin"
                    auth_type: "SHA"
                    auth_pass: "password"
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration with Trap Server using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Create an SNMPv2c configuration only on some devices using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-SNMP"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Delete an SNMP configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-SNMP"
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
from pyafc.services import snmp


def main():
    module_args = {
        "afc_ip": {"type": "str", "required": True},
        "afc_username": {"type": "str", "required": False},
        "afc_password": {"type": "str", "required": False},
        "auth_token": {"type": "str", "required": False},
        "operation": {"type": "str", "required": False},
        "data": {"type": "dict", "required": True},
    }

    ansible_module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    # Get playbook"s arguments
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
        snmp_instance = snmp.Snmp(afc_instance.client, **data)
        if operation == "create":
            message, status, changed = snmp_instance.create_snmp(**data)
        elif operation == "delete":
            message, status, changed = snmp_instance.delete_snmp()
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
