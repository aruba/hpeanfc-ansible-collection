# module: afc_vrf_bgp

Description: This module configures BGP properties on a VRF in the specified fabric.

##### ARGUMENTS

```YAML
afc_ip:
  description: IP address of the HPE ANW Fabric Composer.
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
  description: Auth token from the create session playbook.
  type: str
  required: false
disable_tls_verification:
  description: Disable TLS certificate verification when connecting to AFC. Only
    enable this for AFC instances using self-signed certificates.
  type: bool
  required: false
  default: false
operation:
  description: Operation to be performed with the VRF BGP, enable, update or disable
  type: str
  choices:
  - enable
  - update
  - disable
  required: true
data:
  description: BGP configuration options. Structure is provided in the example.
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
      description: Enables OSPF Redistribution.
      type: bool
      default: false
      required: false
    redistribute_static:
      description: Enables Static Routes Redistribution.
      type: bool
      default: false
      required: false
    redistribute_loopback:
      description: Enables Loopback Redistribution.
      type: bool
      default: false
      required: false
    redistribute_connected:
      description: Enables Connected Redistribution.
      default: false
      type: bool
      required: false
    keepalive_timer:
      description: Keepalive timer.
      type: int
      default: 60
      required: false
    holddown_timer:
      description: Holddown timer.
      type: int
      default: 180
      required: false
    enable:
      description: BGP Enable.
      type: bool
      default: true
      required: false
    bestpath:
      description: BGP Best Path.
      type: bool
      default: true
      required: false
    fast_external_fallover:
      description: Fast External Failover Enable.
      type: bool
      default: true
      required: false
    trap_enable:
      description: Trap Enable.
      type: bool
      default: true
      required: false
    log_neighbor_changes:
      description: Neighbor Logging Enable.
      type: bool
      default: true
      required: false
    deterministic_med:
      description: Deterministic MED Enable.
      type: bool
      default: true
      required: false
    always_compare_med:
      description: Always Compare MED Enable.
      type: bool
      default: true
      required: false
    maximum_paths:
      description: BGP Max Paths. Default to 8
      type: int
      default: 8
      required: false
    networks:
      description: List of BGP Networks to announce
      type: list
      elements: str
      required: false
    neighbors:
      description: List of BGP Neighbors
      type: list
      elements: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
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
```
