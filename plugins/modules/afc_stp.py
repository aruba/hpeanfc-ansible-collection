#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_stp
version_added: "0.0.1"
short_description: Create or delete an STP configuration in the fabric.
description: >
    This module creates or deletes an STP configuration in the fabric.
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
            Operation to be performed on the STP configuration,
            create or delete.
        type: str
        choices:
            - create
            - delete
        required: true
    data:
        description: >
            STP configuration data. Structure is provided in the example.
        type: dict
        suboptions:
            name:
                description: STP Workflow Name
                type: str
                required: true
            fabrics:
                description: List of fabrics
                type: list
                elements: str
                required: false
            config_type:
                description: STP Type
                type: str
                choices:
                    - mstp
                    - rpvst
                default: mstp
                required: false
            configuration:
                description: SNMPv3 user
                type: list
                elements: dict
                suboptions:
                    mstp_config:
                        description: MSTP Configuration elements
                        type: dict
                        suboptions:
                            config_revision:
                                description: MSTP Configuration Revision
                                type: int
                                required: true
                            config_name:
                                description: MSTP Configuration Name
                                type: int
                                required: true
                            instances:
                                description: MSTP Instances configuration
                                type: list
                                elements: dict
                                suboptions:
                                    instance_id:
                                        description: MST region instance ID
                                        type: str
                                        required: true
                                    vlan_ids:
                                        description: MST region VLAN IDs
                                        type: str
                                        required: true
                    rpvst_config:
                        description: RPVST Configuration elements
                        type: dict
                        suboptions:
                            vlan_ids:
                                description: RPVST Instance VLAN IDs
                                type: str
                                required: true
                required: true
        required: true
author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Create STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-STP"
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Test-STP"


-   name: Create STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-STP"
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Test-STP"
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
from pyafc.services import stp


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

    # Get playbook's arguments
    token = None
    ip = ansible_module.params["afc_ip"]
    if "afc_username" in list(ansible_module.params.keys()):
        username = ansible_module.params["afc_username"]
    if "afc_password" in list(ansible_module.params.keys()):
        password = ansible_module.params["afc_password"]
    if "auth_token" in list(ansible_module.params.keys()):
        token = ansible_module.params["auth_token"]
    stp_name = ansible_module.params["stp_name"]
    operation = ansible_module.params["operation"]
    if "stp_data" in list(ansible_module.params.keys()):
        stp_data = ansible_module.params["stp_data"]

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

        if operation == "create":
            stp_instance = stp.STP(
                afc_instance.client,
                name=stp_name,
                **stp_data,
            )
            message, status, changed = stp_instance.create_stp(**stp_data)
        elif operation == "delete":
            stp_instance = stp.STP(afc_instance.client, name=stp_name)
            message, status, changed = stp_instance.delete_stp()
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
