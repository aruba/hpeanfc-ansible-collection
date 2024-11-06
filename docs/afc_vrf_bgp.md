# module: afc_vrf_bgp

Description: This module configures BGP properties on a VRF in the specified fabric.

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
operation:
    description: >
        Operation to be performed with the VRF BGP, update or disable
    type: str
    required: true
fabric_name:
    description: >
        Name of the Fabric where the VRF is located.
    type: str
    required: true
vrf_name:
    description: >
        Name of the VRF where BGP will be configured.
    type: str
    required: true
bgp_data:
    description: >
        BGP configuration options.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Configure BGP on a VRF using username and password
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "update"
        bgp_data:
            as_number: 65000
            name: "Aruba-VRF"
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
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "disable"
        bgp_data:
            enable: false

-   name: Configure BGP on a VRF using token
    arubanetworks.afc.afc_vrf_bgp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "update"
        bgp_data:
            as_number: 65000
            name: "Aruba-VRF"
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
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "disable"
        bgp_data:
            enable: false
```
