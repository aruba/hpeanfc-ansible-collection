# module: afc_route_policy

Description: This module creates or deletes a SFlow configuration in the specified fabric.

##### ARGUMENTS

```YAML
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
rp_object_name:
    description: >
        Name of the route policy object that will be created or deleted from.
    type: str
    required: true
rp_object_type:
    description: >
        Type of the route policy object. Options route_map, prefix_list, community_list, aspath_list.
    type: str
    required: true
rp_object_data:
    description: >
        Object specific data for route_map, prefix_list, community_list, aspath_list.
    type: dict
    required: true
operation:
    description: >
        Operation to be performed on the Route Policy configuration, create or delete.
    type: str
    required: true
```

##### EXAMPLES

```YAML
-   name: Create Route Map using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        rp_object_data:
            switches: '10.10.10.109'
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
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        operation: "delete"

-   name: Create ASPath List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        rp_object_data:
            switches: '10.10.10.109'
            entries:
            -   description: ""
                seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Delete ASPath List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        operation: "delete"

-   name: Create Community List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        rp_object_data:
            switches: '10.10.10.11'
            type: "community-expanded-list"
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
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        operation: "delete"

-   name: Create Prefix List using username and password
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
        rp_object_data:
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
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
        operation: "delete"

-   name: Create Route Map using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        rp_object_data:
            switches: '10.10.10.109'
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
        rp_object_name: "Test-Route-Map"
        rp_object_type: "route_map"
        operation: "delete"

-   name: Create ASPath List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        rp_object_data:
            switches: '10.10.10.109'
            entries:
            -   description: ""
                seq: 10
                action: "deny"
                regex: "_65001$"
        operation: "create"

-   name: Delete ASPath List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        rp_object_name: "Test-ASPath-List"
        rp_object_type: "aspath_list"
        operation: "delete"

-   name: Create Community List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        rp_object_data:
            switches: '10.10.10.11'
            type: "community-expanded-list"
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
        rp_object_name: "Test-Community-List"
        rp_object_type: "community_list"
        operation: "delete"

-   name: Create Prefix List using token
    arubanetworks.afc.afc_route_policy:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
        rp_object_data:
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
        rp_object_name: "Test-Prefix-List"
        rp_object_type: "prefix_list"
        operation: "delete"
```
