# module: afc_ospf

Description: This module creates or deletes an OSPF configuration in the specified fabric.

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
fabric_name:
    description: >
        Name of the Fabric.
    type: str
    required: true
vrf_name:
    description: >
        Name of the VRF in which OSPF objects are to be created or deleted from.
    type: str
    required: true
ospf_object_name:
    description: >
        Name of the OSPF object object that will be created or deleted from.
    type: str
    required: true
ospf_object_type:
    description: >
        Type of the OSPF Object object. Options router, area, interface.
    type: str
    required: true
ospf_object_data:
    description: >
        Object specific data for OSPF router or area or interface.
    type: dict
    required: true
operation:
    description: >
        Operation to be performed on the OSPF object, create or delete.
    type: str
    required: true
```

##### EXAMPLES

```YAML
-   name: Create OSPF Router using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        ospf_object_data:
            instance: "Test-OSPF-Router"
            switches: "10.1.66.11"
            id: 10
            redistribute:
                redistribute_bgp: false
        operation: "create"

-   name: Delete OSPF Router using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        operation: "delete"

-   name: Create OSPF Area using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        ospf_object_data:
            ospf_router: "Test-OSPF-Router"
            switches: "10.1.66.11"
        operation: "create"

-   name: Delete OSPF Area using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        operation: "delete"

-   name: Create OSPF Interface using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
        ospf_object_data:
            router: "10.10.10.254"
            area: "0.0.0.1"
            interface: "1/1/29"
            network_type: "ospf_iftype_pointopoint"
        operation: "create"

-   name: Delete OSPF Interface using username and password
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
        operation: "delete"



-   name: Create OSPF Router using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        ospf_object_data:
            instance: "Test-OSPF-Router"
            switches: "10.1.66.11"
            id: 10
            redistribute:
                redistribute_bgp: false
        operation: "create"

-   name: Delete OSPF Router using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Router"
        ospf_object_type: "router"
        operation: "delete"

-   name: Create OSPF Area using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        ospf_object_data:
            ospf_router: "Test-OSPF-Router"
            switches: "10.1.66.11"
        operation: "create"

-   name: Delete OSPF Area using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Area"
        ospf_object_type: "area"
        operation: "delete"

-   name: Create OSPF Interface using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
        ospf_object_data:
            router: "10.10.10.254"
            area: "0.0.0.1"
            interface: "1/1/29"
            network_type: "ospf_iftype_pointopoint"
        operation: "create"

-   name: Delete OSPF Interface using token
    arubanetworks.afc.afc_ospf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        ospf_object_name: "Test-OSPF-Interface"
        ospf_object_type: "interface"
        operation: "delete"
```
