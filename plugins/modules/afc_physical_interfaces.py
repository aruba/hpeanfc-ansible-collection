#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_physical_interfaces
version_added: "0.0.1"
short_description: Configure Physical Ports.
description: >
    This module is used to configure physical ports.
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
            Port configuration data. Structure is provided in the example.
        type: list
        elements: dict
        suboptions:
            switch:
                description: Switch IP Address
                type: str
                required: true
            ports_config:
                description: List of physical ports on that switch
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description: Port ID
                        type: str
                        required: true
                    ungrouped_vlans:
                        description: set of VLANs to be configured
                        type: str
                        required: false
                    native_vlan:
                        description: Native VLAN
                        type: str
                        required: false
                    tagged:
                        description: tagged Native VLAN
                        type: bool
                        required: false
                    admin_state:
                        description: Administrative State
                        type: str
                        choices:
                            - enabled
                            - disabled
                        required: false
                    description:
                        description: Port's description
                        type: str
                        required: false
                    speed:
                        description: Port's speed
                        type: str
                        required: false
                    mtu:
                        description: Port's MTU
                        type: str
                        required: false
                    qsfp_mode:
                        description: Port's split
                        type: str
                        required: false
                    routed:
                        description: Bridging or Routing mode
                        type: bool
                        required: false
                    bpdu_filter:
                        description: Enable BPDU Filtering
                        type: str
                        required: false
                    bpdu_guard:
                        description: Enable BPDU Guard
                        type: str
                        required: false
                    root_guard:
                        description: Enable Root Guard
                        type: str
                        required: false
                    loop_guard:
                        description: Enable Loop Guard
                        type: str
                        required: false
                    tcn_guard:
                        description: Enable TCN Guard
                        type: str
                        required: false
                    admin_port_type:
                        description: Enable STP Admin Port Type
                        type: str
                        choices:
                            - admin-network
                            - admin-edge
                        required: false
                    rpvst_guard:
                        description: Enable RPVST Guard
                        type: str
                        required: false
                    rpvst_filter:
                        description: Enable RPVST Filtering
                        type: str
                        required: false
author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Configure Ports using username and password
    arubanetworks.afc.afc_physical_interfaces:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            - switch: 10.10.10.7
              ports_config:
                - name: 1/1/37
                  native_vlan: 250
                - name: 1/1/38
                  native_vlan: 250
            - switch: 10.10.10.8
              ports_config:
                - name: 1/1/37
                  ungrouped_vlans: "250-252"
                  native_vlan: 250
                - name: 1/1/38
                  ungrouped_vlans: "250-252"
                  native_vlan: 250

-   name: Configure Ports using token
    arubanetworks.afc.afc_physical_interfaces:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            - switch: 10.10.10.7
              ports_config:
                - name: 1/1/37
                  native_vlan: 250
                - name: 1/1/38
                  native_vlan: 250
            - switch: 10.10.10.8
              ports_config:
                - name: 1/1/37
                  ungrouped_vlans: "250-252"
                  native_vlan: 250
                - name: 1/1/38
                  ungrouped_vlans: "250-252"
                  native_vlan: 250

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
from pyafc.ports import ports


def main():
    module_args = {
        "afc_ip": {"type": "str", "required": True},
        "afc_username": {"type": "str", "required": False},
        "afc_password": {"type": "str", "required": False},
        "auth_token": {"type": "str", "required": False},
        "data": {"type": "raw", "required": True},
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

    afc_instance = instantiate_afc_object(data=auth_data)

    result = {"changed": False}

    if ansible_module.check_mode:
        ansible_module.exit_json(**result)

    status = False
    changed = False
    message = ""

    afc_instance = instantiate_afc_object(data=auth_data)

    if afc_instance.afc_connected:
        message, status, changed = ports.PORT.configure_multiple_physical_port(
            afc_instance.client,
            data,
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
