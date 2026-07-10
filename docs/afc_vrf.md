# module: afc_vrf

Description: This module creates or deletes a VRF in the specified fabric.

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
  description: Operation to be performed on the VRF, create delete or reapply.
  type: str
  choices:
  - create
  - reapply
  - delete
  required: true
data:
  description: VRF specific data. Structure provided in the example.
  type: dict
  suboptions:
    name:
      description: VRF Name
      type: str
      required: true
    fabric:
      description: Fabric Name
      type: str
      required: true
    vni:
      description: L3VNI attached to the VRF
      type: int
      required: false
    route_distinguisher:
      description: Route Distinguisher.
      type: str
      default: loopback1:1
      required: true
    max_cps_mode:
      description: Specific to HPE ANW 10000. Maximum Connections per Seconds
        mode.
      type: str
      choices:
      - unlimited
      - enabled
      default: unlimited
      required: false
    max_cps:
      description: Specific to HPE ANW 10000. Maximum Connections per Seconds.
      type: int
      required: false
    max_sessions_mode:
      description: Specific to HPE ANW 10000. Maximum Sessions mode.
      type: str
      choices:
      - unlimited
      - enabled
      default: unlimited
      required: false
    max_sessions:
      description: Specific to HPE ANW 10000. Maximum number of Sessions.
      type: int
      required: false
    allow_session_reuse:
      description: Specific to HPE ANW 10000. Allow Session Reuse.
      type: bool
      default: false
      required: false
    connection_tracking_mode:
      description: Specific to HPE ANW 10000. Connection tracking enabled.
      type: bool
      default: false
      required: false
    route_target:
      description: Route Target specific data.
      type: dict
      required: false
      suboptions:
        primary_route_target:
          description: Primary Route Target
          type: dict
          suboptions:
            as_number:
              description: AS Number
              type: str
              required: false
            address_family:
              description: Address Family
              type: str
              choices:
              - evpn
              - ipv4_unicast
              - ipv6_unicast
              required: false
            route_mode:
              description: Route Mode
              type: str
              choices:
              - import
              - export
              - both
              required: false
          required: false
        secondary_route_targets:
          description: Secondary Route Targets, as a list
          type: list
          elements: dict
          suboptions:
            as_number:
              description: AS Number
              type: str
              required: false
            address_family:
              description: Address Family
              type: str
              choices:
              - evpn
              - ipv4_unicast
              - ipv6_unicast
              required: false
            route_mode:
              description: Route Mode
              type: str
              choices:
              - import
              - export
              - both
              required: false
          required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create VRF using username and password
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"
            vni: 10000
            route_target:
                primary_route_target:
                    as_number: "65000:1"
                    address_family: "evpn"
                    route_mode: "both"
                secondary_route_targets:
                    -   as_number: "1:1"
                        address_family: "evpn"
                        route_mode: "both"

-   name: Reapply VRF using username and password
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reapply"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"

-   name: Delete VRF using username and password
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"

-   name: Create VRF using token
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"
            vni: 10000
            route_target:
                primary_route_target:
                    as_number: "65000:1"
                    address_family: "evpn"
                    route_mode: "both"
                secondary_route_targets:
                    -   as_number: "1:1"
                        address_family: "evpn"
                        route_mode: "both"

-   name: Reapply VRF using username and password
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reapply"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"

-   name: Delete VRF using token
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Aruba-VRF"
            fabric: "Aruba-Fabric"
```
