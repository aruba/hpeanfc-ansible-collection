# module: afc_underlay

Description: This module applies an underlay configuration in the specified fabric and vrf.

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
  description: Operation to be performed on the Underlay, create or reapply.
  type: str
  choices:
  - create
  - reapply
  required: true
data:
  description: Underlay data. The structure is provided in the example.
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
    ipv4_address:
      description: IPv4 Resource Pool used to create Loopbacks
      type: int
      required: true
    transit_vlan:
      description: OSPF Transit VLAN between VSX peers
      type: int
      required: true
    underlay_type:
      description: Underlay's type
      type: str
      choices:
      - OSPF
      - EBGP
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create an underlay configuration using username and password
    arubanetworks.afc.afc_underlay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-underlay"
            fabric: "Aruba-Fabric"
            ipv4_address: 'IP POOL'
            transit_vlan: 120
            underlay_type: 'OSPF'

-   name: Reapply an underlay configuration using username and password
    arubanetworks.afc.afc_underlay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reapply"
        data:
            name: "Test-underlay"
            fabric: "Aruba-Fabric"

-   name: Create an underlay configuration using token
    arubanetworks.afc.afc_underlay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-underlay"
            fabric: "Aruba-Fabric"
            ipv4_address: 'IP POOL'
            transit_vlan: 120
            underlay_type: 'OSPF'

-   name: Reapply an underlay configuration using token
    arubanetworks.afc.afc_underlay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reapply"
        data:
            name: "Test-underlay"
            fabric: "Aruba-Fabric"
```
