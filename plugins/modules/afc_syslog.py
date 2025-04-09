#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_syslog
version_added: "0.0.1"
short_description: Create or delete a syslog client configuration.
description: >
    This module creates or deletes a syslog client configuration.
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
            Operation to be performed on the Syslog configuration,
            create or delete.
        type: str
        choices:
            - create
            - delete
        required: true
    data:
        description: >
            Syslog client configuration data as per the example below.
        type: str
        suboptions:
            name:
                description: DHCP Relay Config name
                type: str
                required: true
            description:
                description: DHCP Relay Config description
                type: str
                required: false
            facility:
                description: >
                    Facility level.
                    Set to USER when syslog is created only
                    for HPE ANW Fabric Composer
                type: str
                choices:
                    - LOCAL0
                    - LOCAL1
                    - LOCAL2
                    - LOCAL3
                    - LOCAL4
                    - LOCAL5
                    - LOCAL6
                    - LOCAL7
                    - USER
                required: false
            logging_persistent_storage:
                description: >
                    Enables Persistent Storage
                type: dict
                suboptions:
                    severity:
                        description: >
                            Log Severity.
                        type: str
                        choices:
                            - EMERG
                            - ALERT
                            - CRIT
                            - ERROR
                            - WARNING
                            - NOTICE
                            - INFO
                            - DEBUG
                        default: 'INFO'
                        required: false
                    enable:
                        description: >
                            Enable Persistent Storage.
                        type: bool
                        default: true
                        required: false
                required: false
            entry_list:
                description: >
                    Enables Persistent Storage
                type: list
                elements: dict
                suboptions:
                    host:
                        description: Syslog Server IPv4/v6 Address or hostname.
                        type: str
                        required: true
                    port:
                        description: Syslog Server Port.
                        type: int
                        required: false
                    severity:
                        description: >
                            Log Severity.
                        type: str
                        choices:
                            - EMERG
                            - ALERT
                            - CRIT
                            - ERROR
                            - WARNING
                            - NOTICE
                            - INFO
                            - DEBUG
                        default: 'INFO'
                        required: false
                    include_auditable_events:
                        description: >
                            Specifies whether auditable events should be
                            transmitted to the remote syslog server
                        type: bool
                        default: true
                        required: false
                    unsecure_tls_renegotiation:
                        description: >
                            Enable TLS session with syslog server which
                            does not support secure renegotiation.
                        type: bool
                        default: true
                        required: false
                    tls_auth_mode:
                        description: >
                            TLS authentication mode used to
                            authenticate the server
                        type: str
                        choices:
                            - certificate
                            - subject-name
                        required: false
                    transport:
                        description: >
                            Transport layer protocol used
                            to forward messages to the server.
                        type: str
                        choices:
                            - udp
                            - tcp
                            - tls
                        default: udp
                        required: false
                required: true
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
        required: true
author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Create syslog configuration using username and password
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-Syslog"
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - "Test-Fabric"

-   name: Delete syslog configuration using username and password
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Syslog"
        operation: "delete"

-   name: Create syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-Syslog"
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - "Test-Fabric"

-   name: Delete syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Syslog"
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
from pyafc.services import syslog


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
        syslog_instance = syslog.Syslog(afc_instance.client, **data)
        if operation == "create":
            message, status, changed = syslog_instance.create_syslog(**data)
        elif operation == "delete":
            message, status, changed = syslog_instance.delete_syslog()
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
