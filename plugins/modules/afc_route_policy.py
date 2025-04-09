#!/usr/bin/python

# (C) Copyright 2020-2025 Hewlett Packard Enterprise Development LP.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: afc_route_policy
version_added: "0.0.1"
short_description: >
    Create or delete a Route Policy.
    Can be either Route Maps, AS Path List, Prefix List or Community LIst
description: >
    This module creates or deletes a Route Policy configuration.
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
            Operation to be performed on the Route Policy configuration,
            create or delete.
        type: str
        choices:
            - create
            - delete
        required: true
    data:
        description: >
            Object specific data for route_map, prefix_list, community_list,
            aspath_list. Structure is provided in the example.
        type: dict
        required: true
        suboptions:
            name:
                description: Route Policy Name
                type: str
                required: true
            type:
                description: Route Policy type
                type: str
                choices:
                    - route_map
                    - aspath_list
                    - prefix_list
                    - community_list
                required: true
            description:
                description: Route Policy description
                type: str
                required: false
            object_type:
                description: >
                    Community List Specific. Community List type
                type: str
                choices:
                    - community-list
                    - community-expanded-list
                    - extcommunity-list
                    - extcommunity-expanded-list
                required: false
            entries:
                description: Entries composing the Route Policy
                type: list
                elements: dict
                suboptions:
                    seq:
                        description: Sequence Number
                        type: str
                        required: true
                    action:
                        description: entry's action
                        type: str
                        choices:
                            - permit
                            - deny
                        required: true
                    description:
                        description: Entry's description
                        type: str
                        required: false
                    regex:
                        description: >
                            As Path List specific.
                            A regular-expression to match the BGP AS paths
                        type: str
                        required: false
                    match_string:
                        description: >
                            Community List specific.
                            String to be matched with
                        type: str
                        required: false
                    prefix:
                        description: >
                            Prefix List specific.
                            Any prefix match
                        type: str
                        required: false
                    ge:
                        description: >
                            Prefix List specific.
                            Prefix minimum match length, 0 for unspecified.
                            Must be greater than initial prefix lengt
                        type: int
                        required: false
                    le:
                        description: >
                            Prefix List specific.
                            Prefix maximum match length, 0 for unspecified.
                            Must be greater than initial prefix length
                        type: int
                        required: false
                    route_map_continue:
                        description: >
                            Route Map specific.
                            Sequence number to be executed next.
                            Must be greater than the current sequence number
                        type: int
                        required: false
                    match_as_path:
                        description: >
                            Route Map specific.
                            Match routes based on BGP AS path list name
                        type: str
                        required: false
                    match_community_list:
                        description: >
                            Route Map specific.
                            Match BGP community list name
                        type: str
                        required: false
                    match_extcommunity_list:
                        description: >
                            Route Map specific.
                            Match extended BGP community list name
                        type: str
                        required: false
                    match_local_preference:
                        description: >
                            Route Map specific.
                            Match routes with the specific local
                            preference value.
                        type: int
                        required: false
                    match_interface:
                        description: >
                            Route Map specific.
                            Match interface (port) name
                        type: str
                        required: false
                    match_ipv4_next_hop_address:
                        description: >
                            Route Map specific.
                            Match next-hop IPv4 address of the route.
                        type: str
                        required: false
                    match_ipv4_prefix_list:
                        description: >
                            Route Map specific.
                            Match entries of IPv4 prefix-list name
                        type: str
                        required: false
                    match_ipv4_next_hop_prefix_list:
                        description: >
                            Route Map specific.
                            Match entries of IP prefix-list name
                        type: str
                        required: false
                    match_ipv4_route_source_prefix_list:
                        description: >
                            Route Map specific.
                            Match route-source of route from prefix list name
                        type: str
                        required: false
                    match_metric:
                        description: >
                            Route Map specific.
                            Match routes with the specific metric value
                        type: int
                        required: false
                    match_origin:
                        description: >
                            Route Map specific.
                            Match BGP origin code
                        type: str
                        choices:
                            - egp
                            - igp
                            - incomplete
                        required: false
                    match_route_type:
                        description: >
                            Route Map specific.
                            Match the specified route type
                        type: str
                        choices:
                            - external_type1
                            - external_type2
                        required: false
                    match_source_protocol:
                        description: >
                            Route Map specific.
                            Match the specified source protocol of the routes
                        type: str
                        choices:
                            - static
                            - connected
                            - ospf
                            - bgp
                        required: false
                    match_tag:
                        description: >
                            Route Map specific.
                            Match the specified tag in the route.
                        type: int
                        required: false
                    match_vni:
                        description: >
                            Route Map specific.
                            Match routes with specific Virtual Network ID
                            value.
                        type: int
                        required: false
                    set_as_path_exclude:
                        description: >
                            Route Map specific.
                            Excludes AS number from the AS path
                        type: str
                        required: false
                    set_as_path_prepend:
                        description: >
                            Route Map specific.
                            AS numbers to prepend to the AS path
                        type: str
                        required: false
                    set_community:
                        description: >
                            Route Map specific.
                            Set BGP community attribute
                        type: str
                        required: false
                    set_evpn_router_mac:
                        description: >
                            Route Map specific.
                            Set the Router MAC in the EVPN updates
                        type: str
                        required: false
                    set_extcommunity_rt:
                        description: >
                            Route Map specific.
                            Set the route target extended community of a BGP
                            route
                        type: str
                        required: false
                    set_dampening_half_life:
                        description: >
                            Route Map specific.
                            Amount of time (in minutes) that must elapse to
                            reduce the penalty by one half
                        type: int
                        required: false
                    set_dampening_max_suppress_time:
                        description: >
                            Route Map specific.
                            The longest amount of time (in minutes) that a
                            route can be suppressed
                        type: int
                        required: false
                    set_dampening_reuse:
                        description: >
                            Route Map specific.
                            If the penalty is less than the reuse limit,
                            a suppressed route that is up will no longer be
                            suppressed
                        type: int
                        required: false
                    set_dampening_suppress:
                        description: >
                            Route Map specific.
                            If the penalty is greater than the suppress
                            limit, the route is suppressed
                        type: int
                        required: false
                    set_next_hop:
                        description: >
                            Route Map specific.
                            Set next-hop for IPv4
                        type: str
                        required: false
                    set_local_preference:
                        description: >
                            Route Map specific.
                            Set BGP local preference path attribute
                        type: int
                        required: false
                    set_metric:
                        description: >
                            Route Map specific.
                            Set Metric value for destination routing protocol
                        type: int
                        required: false
                    set_metric_type:
                        description: >
                            Route Map specific.
                            Set BGP metric-type of a route
                        type: str
                        choices:
                            - external_type1
                            - external_type2
                        required: false
                    set_origin:
                        description: >
                            Route Map specific.
                            Set the origin attribute of a local BGP route
                        type: str
                        choices:
                            - egp
                            - igp
                            - incomplete
                        required: false
                    set_tag:
                        description: >
                            Route Map specific.
                            Tag value for destination routing protocol
                        type: int
                        required: false
                    set_weight:
                        description: >
                            Route Map specific.
                            Set BGP weight for routing table
                        type: int
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
-   name: Create Route Map on specific devices using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Route-Map"
            type: "route_map"
            switches:
            -   "10.10.10.109"
            entries:
            -   seq: 10
                action: "deny"
                description: "ee"
                route_map_continue: 20
                match_vni: 10100
                set_origin: "igp"
            -   seq: 20
                action: "deny"
                match_tag: 100
        operation: "create"

-   name: Create Route Map on Fabric using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Route-Map"
            type: "route_map"
            fabrics:
            -   "Fabric1"
            entries:
            -   seq: 10
                action: "deny"
                description: "ee"
                route_map_continue: 20
                match_vni: 10100
                set_origin: "igp"
            -   seq: 20
                action: "deny"
                match_tag: 100
        operation: "create"

-   name: Delete Route Map using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Route-Map"
            type: "route_map"
        operation: "delete"

-   name: Create ASPath List on specific devices using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-ASPath-List"
            type: "aspath_list"
            switches:
            -   "10.10.10.109"
            description: ""
            entries:
            -   seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Create ASPath List on Fabric using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-ASPath-List"
            type: "aspath_list"
            fabrics:
            -   "Fabric1"
            description: ""
            entries:
            -   seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Delete ASPath List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-ASPath-List"
            type: "aspath_list"
        operation: "delete"

-   name: Create Community List on specific devices using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Community-List"
            type: "community_list"
            object_type: "community-expanded-list"
            switches:
                - "10.10.10.11"
            entries:
                -   description: ""
                    seq: 10
                    action: "deny"
                    match_string: "internet"
        operation: "create"

-   name: Create Community List on Fabric using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Community-List"
            type: "community_list"
            object_type: "community-expanded-list"
            fabrics:
            -   "Fabric1"
            entries:
                -   description: ""
                    seq: 10
                    action: "deny"
                    match_string: "internet"
        operation: "create"

-   name: Delete Community List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Community-List"
            type: "community_list"
        operation: "delete"

-   name: Create Prefix List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Prefix-List"
            type: "prefix_list"
            seq: 20
            action: "permit"
            prefix:
                address: "10.10.20.0"
                prefix_length: 24
        operation: "create"

-   name: Create Prefix List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Prefix-List"
            type: "prefix_list"
            seq: 20
            action: "permit"
            prefix:
                address: "10.10.20.0"
                prefix_length: 24
        operation: "create"

-   name: Delete Prefix List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Prefix-List"
            type: "prefix_list"
        operation: "delete"

-   name: Create Route Map using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Route-Map"
            type: "route_map"
            switches:
            -   "10.10.10.109"
            entries:
            -   seq: 10
                action: "deny"
                description: "ee"
                route_map_continue: 20
                match_vni: 10100
                set_origin: "igp"
            -   seq: 20
                action: "deny"
                match_tag: 100
        operation: "create"

-   name: Create Route Map using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Route-Map"
            type: "route_map"
            switches:
            -   "10.10.10.109"
            entries:
            -   seq: 10
                action: "deny"
                description: "ee"
                route_map_continue: 20
                match_vni: 10100
                set_origin: "igp"
            -   seq: 20
                action: "deny"
                match_tag: 100
        operation: "create"

-   name: Delete Route Map using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Route-Map"
            type: "route_map"
        operation: "delete"

-   name: Create ASPath List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-ASPath-List"
            type: "aspath_list"
            switches:
            -   "10.10.10.109"
            description: ""
            entries:
            -   seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Delete ASPath List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-ASPath-List"
            type: "aspath_list"
        operation: "delete"

-   name: Create Community List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Community-List"
            type: "community_list"
            object_type: "community-expanded-list"
            switches:
                - "10.10.10.11"
            entries:
                -   description: ""
                    seq: 10
                    action: "deny"
                    match_string: "internet"
        operation: "create"

-   name: Delete Community List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Community-List"
            type: "community_list"
        operation: "delete"

-   name: Create Prefix List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Prefix-List"
            type: "prefix_list"
            seq: 20
            action: "permit"
            prefix:
                address: "10.10.20.0"
                prefix_length: 24
        operation: "create"

-   name: Delete Prefix List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Prefix-List"
            type: "prefix_list"
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
from pyafc.route_policies import (
    as_path_lists,
    community_lists,
    prefix_lists,
    route_maps,
)


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
        if operation == "create":
            if data["type"] == "route_map":
                route_map_instance = route_maps.RouteMap(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = route_map_instance.create_routemap(
                    **data,
                )
            elif data["type"] == "aspath_list":
                aspath_list_instance = as_path_lists.ASPathList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    aspath_list_instance.create_aspath_list(
                        **data,
                    )
                )
            elif data["type"] == "prefix_list":
                prefix_list_instance = prefix_lists.PrefixList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    prefix_list_instance.create_prefix_list(
                        **data,
                    )
                )
            elif data["type"] == "community_list":
                community_list_instance = community_lists.CommunityList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    community_list_instance.create_community_list(
                        **data,
                    )
                )
            else:
                message = "Route Policy type not supported - No action taken"
        elif operation == "delete":
            if data["type"] == "route_map":
                route_map_instance = route_maps.RouteMap(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = route_map_instance.delete_routemap()
            elif data["type"] == "aspath_list":
                aspath_list_instance = as_path_lists.ASPathList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    aspath_list_instance.delete_aspath_list()
                )
            elif data["type"] == "prefix_list":
                prefix_list_instance = prefix_lists.PrefixList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    prefix_list_instance.delete_prefix_list()
                )
            elif data["type"] == "community_list":
                community_list_instance = community_lists.CommunityList(
                    afc_instance.client,
                    **data,
                )
                message, status, changed = (
                    community_list_instance.delete_community_list()
                )
            else:
                message = "Route Policy type not supported - No action taken"
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
