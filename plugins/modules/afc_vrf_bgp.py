#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_vrf_bgp
version_added: "0.0.1"
short_description: Update BGP Properties or disable BGP on VRF.
description: >
    This module configures BGP properties on a VRF in the specified fabric.
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
            Operation to be performed with the VRF BGP, enable, update or
            disable
        type: str
        choices:
            - enable
            - update
            - disable
        required: true
    data:
        description: >
            BGP configuration options. Structure is provided in the example.
        type: dict
        suboptions:
            as_number:
                description: AS Number
                type: str
                required: true
            description:
                description: Description
                type: str
                required: false
            router_id:
                description: BGP Router ID
                type: str
                required: false
            redistribute_ospf:
                description: >
                    Enables OSPF Redistribution.
                type: bool
                default: false
                required: false
            redistribute_static:
                description: >
                    Enables Static Routes Redistribution.
                type: bool
                default: false
                required: false
            redistribute_loopback:
                description: >
                    Enables Loopback Redistribution.
                type: bool
                default: false
                required: false
            redistribute_connected:
                description: >
                    Enables Connected Redistribution.
                default: false
                type: bool
                required: false
            keepalive_timer:
                description: >
                    Keepalive timer.
                type: int
                default: 60
                required: false
            holddown_timer:
                description: >
                    Holddown timer.
                type: int
                default: 180
                required: false
            enable:
                description: >
                    BGP Enable.
                type: bool
                default: true
                required: false
            bestpath:
                description: >
                    BGP  Best Path.
                type: bool
                default: true
                required: false
            fast_external_fallover:
                description: >
                    Fast External Failover Enable.
                type: bool
                default: true
                required: false
            trap_enable:
                description: >
                    Trap Enable.
                type: bool
                default: true
                required: false
            log_neighbor_changes:
                description: >
                    Neighbor Logging Enable.
                type: bool
                default: true
                required: false
            deterministic_med:
                description: >
                    Deterministic MED Enable.
                type: bool
                default: true
                required: false
            always_compare_med:
                description: >
                    Always Compare MED Enable.
                type: bool
                default: true
                required: false
            maximum_paths:
                description: >
                    BGP Max Paths.
                    Default to 8
                type: int
                default: 8
                required: false
            networks:
                description: >
                    List of BGP Networks to announce
                type: list
                elements: str
                required: false
            neighbors:
                description: >
                    List of BGP Neighbors
                type: list
                elements: str
                required: false
        required: true
author: Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Enable BGP on a VRF using username and password
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "enable"
        data:
            as_number: 65000
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            redistribute_ospf: true
            redistribute_connected: true
            redistribute_static: true
            redistribute_loopback: true
            enable: true
            trap_enable: true
            log_neighbor_changes: true
            fast_external_fallover: true
            maximum_paths: 8
            deterministic_med: true
            bestpath: true
            always_compare_med: true
            keepalive_timer: 60
            holddown_timer: 90

-   name: Disable BGP on a VRF using username and password
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "disable"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: false

-   name: Update BGP configuration on a VRF using username and password
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "update"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            redistribute_loopback: true
            trap_enable: false

-   name: Update BGP configuration on a VRF using token
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "update"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            redistribute_loopback: true
            trap_enable: false

-   name: Configure BGP on a VRF using token
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "enable"
        data:
            as_number: 65000
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            redistribute_ospf: true
            redistribute_connected: true
            redistribute_static: true
            redistribute_loopback: true
            enable: true
            trap_enable: true
            log_neighbor_changes: true
            fast_external_fallover: true
            maximum_paths: 8
            deterministic_med: true
            bestpath: true
            always_compare_med: true
            keepalive_timer: 60
            holddown_timer: 90

-   name: Disable BGP on a VRF using token
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "disable"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: false
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
from pyafc.fabric import fabric
from pyafc.vrf import vrf


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
    operation = ansible_module.params["operation"]
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
        fabric_instance = fabric.Fabric(
            afc_instance.client,
            name=data["fabric"],
        )
        if fabric_instance.uuid:
            vrf_instance = vrf.Vrf(
                afc_instance.client,
                name=data["vrf"],
                fabric_uuid=fabric_instance.uuid,
            )
            if vrf_instance.uuid:
                if operation == "enable":
                    message, status, changed = vrf_instance.update_bgp_vrf(
                        **data,
                    )
                elif operation == "update":
                    message, status, changed = (
                        vrf_instance.update_bgp_config_vrf(**data)
                    )
                elif operation == "disable":
                    message, status, changed = (
                        vrf_instance.update_bgp_config_vrf(enable=False)
                    )
            else:
                message = "VRF not found - No action taken"
                status = False
                changed = False
        else:
            message = "Fabric not found - No action taken"
            status = False
            changed = False

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
