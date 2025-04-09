#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_ospf
version_added: "0.0.1"
short_description: Create or delete an OSPF configuration.
description:
  - This module creates or deletes an OSPF configuration.
options:
  afc_ip:
    description:
      - IP address of the HPE ANW Fabric Composer.
    type: str
    required: true
  afc_username:
    description:
      - User account having write permission on the HPE ANW Fabric Composer.
    type: str
    required: false
  afc_password:
    description:
      - Password of the user account.
    type: str
    required: false
  auth_token:
    description:
      - Auth token from the create session playbook.
    type: str
    required: false
  operation:
    description:
      - Operation to be performed on the OSPF object, create or delete.
    type: str
    choices: [create]
    required: true
  data:
    description:
      - Object specific data for OSPF router, area, or interface.
    type: dict
    required: true
    suboptions:
      type:
        description:
          - Type of OSPF item.
        type: str
        choices: [router, area, interface]
        required: true
      fabric:
        description:
          - Fabric Name.
        type: str
        required: true
      vrf:
        description:
          - VRF Name.
        type: str
        required: true
      name:
        description:
          - OSPF Workflow Name.
        type: str
        required: true
      enable:
        description:
          - OSPF Router's Status.
        type: bool
        default: true
        required: false
      id:
        description:
          - OSPF Router ID.
        type: int
        default: 1
        required: false
      redistribute:
        description:
          - OSPF Router specific. OSPF Redistribution rule.
        type: dict
        required: false
        suboptions:
          redistribute_static:
            description:
              - Redistribute Static Routes.
            type: bool
            default: false
            required: false
          redistribute_connected:
            description:
              - Redistribute Connected.
            type: bool
            default: true
            required: false
          redistribute_local:
            description:
              - Redistribute Local.
            type: bool
            default: true
            required: false
          redistribute_bgp:
            description:
              - Redistribute BGP.
            type: bool
            default: false
            required: false
      redistribute_route_map:
        description:
          - OSPF Router specific. OSPF Redistribution Route Map rule.
        type: dict
        required: false
        suboptions:
          redistribute_connected_route_map:
            description:
              - Redistribute Connected Routes Route Map's name.
            type: str
            required: false
          redistribute_local_route_map:
            description:
              - Redistribute Local Routes Route Map's name.
            type: str
            required: false
      maximum_paths:
        description:
          - OSPF Router Specific. OSPF Max Paths.
        type: int
        default: 8
        required: false
      max_metric_router_lsa:
        description:
          - Advertise Router-LSAs with maximum metric value.
        type: bool
        default: true
        required: false
      max_metric_include_stub:
        description:
          - Advertise Router-LSAs with max metric for stub links.
        type: bool
        default: true
        required: false
      max_metric_on_startup:
        description:
          - Time in seconds to advertise Router-LSAs with max metric after startup.
        type: int
        required: false
      passive_interface_default:
        description:
          - Configure all OSPF-enabled interfaces as passive.
        type: bool
        default: true
        required: false
      trap_enable:
        description:
          - Enable OSPF SNMP Traps.
        type: bool
        default: true
        required: false
      gr_ignore_lost_interface:
        description:
          - Ignore lost OSPF interfaces during graceful restart.
        type: bool
        default: false
        required: false
      gr_restart_interval:
        description:
          - Max interval in seconds that another router should wait.
        type: int
        required: false
      distance:
        description:
          - Configure OSPF administrative distance.
        type: int
        required: false
      default_metric:
        description:
          - Configure default metric of redistributed routes.
        type: int
        required: false
      default_information:
        description:
          - Allow a default route to be advertised.
        type: str
        choices: [disable, originate, always_originate]
        default: disable
        required: false
      area_id:
        description:
          - OSPF Area ID.
        type: int
        default: 0
        required: false
      area_type:
        description:
          - OSPF Area Type.
        type: str
        choices: [standard, nssa, stub, stub_no_summary, nssa_no_summary]
        default: standard
        required: false
      priority:
        description:
          - OSPF Priority.
        type: int
        default: 1
        required: false
      process:
        description:
          - OSPF Process ID.
        type: int
        default: 1
        required: false
      hello_interval:
        description:
          - Interval period for hello messages in seconds.
        type: int
        default: 10
        required: false
      dead_interval:
        description:
          - Dead period for hello messages in seconds.
        type: int
        default: 40
        required: false
      mtu_size:
        description:
          - OSPF MTU size in bytes.
        type: int
        default: 1500
        required: false
      ignore_mtu_mismatch:
        description:
          - Ignore MTU mismatch.
        type: bool
        default: false
        required: false
      passive_mode:
        description:
          - Enable OSPF Passive Interface.
        type: bool
        default: false
        required: false
      authentication_value:
        description:
          - Simple-text authentication value.
        type: str
        required: false
      md5_list:
        description:
          - MD5 authentication key value pairs.
        type: list
        elements: str
        required: false
      authentication_type:
        description:
          - Authentication type.
        type: str
        choices: [simple-text, message-digest]
        required: false
      network_type:
        description:
          - OSPF Network type.
        type: str
        choices:
          - ospf_iftype_pointopoint
          - ospf_iftype_broadcast
          - ospf_iftype_loopback
          - ospf_iftype_none
        required: true
      bfd:
        description:
          - Enable Bidirectional Forwarding Detection.
        type: bool
        required: false
      switches:
        description:
          - List of Switches.
        type: list
        elements: str
        required: true
author:
  - Aruba Networks (@ArubaNetworks)
"""

EXAMPLES = r"""
-   name: Create OSPF Router using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            type: router
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Router'
            switches:
                - '10.10.10.11'
                - '10.10.10.12'
            id: 1
            redistribute:
                redistribute_bgp: false

-   name: Create OSPF Area using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Area'
            type: area
            ospf_router: "Test-OSPF-Router"
            switches:
                - '10.10.10.11'
                - '10.10.10.12'
            area_id: 1

-   name: Create OSPF Interface using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Interface'
            router: '10.10.10.11'
            type: interface
            area: "0.0.0.0"
            interface: "1/1/14"
            network_type: "ospf_iftype_pointopoint"
            process: 1

-   name: Create OSPF Router using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            type: router
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Router'
            switches:
                - '10.10.10.11'
                - '10.10.10.12'
            id: 1
            redistribute:
                redistribute_bgp: false

-   name: Create OSPF Area using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Area'
            type: area
            ospf_router: "Test-OSPF-Router"
            switches:
                - '10.10.10.11'
                - '10.10.10.12'
            area_id: 1

-   name: Create OSPF Interface using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 'Test-OSPF-Interface'
            router: '10.10.10.11'
            type: interface
            area: "0.0.0.0"
            interface: "1/1/14"
            network_type: "ospf_iftype_pointopoint"
            process: 1
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
    data = ansible_module.params["data"]
    operation = ansible_module.params["operation"]

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
            afc_instance.client, name=data["fabric"]
        )
        if fabric_instance.uuid:
            vrf_instance = vrf.Vrf(
                afc_instance.client,
                name=data["vrf"],
                fabric_uuid=fabric_instance.uuid,
            )
            if vrf_instance.uuid:
                if operation == "create":
                    if data["type"] == "router":
                        message, status, changed = (
                            vrf_instance.create_ospf_router(
                                **data,
                            )
                        )
                    elif data["type"] == "area":
                        message, status, changed = (
                            vrf_instance.create_ospf_area(
                                **data,
                            )
                        )
                    elif data["type"] == "interface":
                        message, status, changed = (
                            vrf_instance.create_ospf_interface(
                                **data,
                            )
                        )
                else:
                    message = "Operation not supported - No action taken"
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
