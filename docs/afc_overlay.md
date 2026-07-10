# module: afc_overlay

Description: This module applies an overlay configuration in the specified fabric and vrf.

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
  description: Operation to be performed on the Overlay, create or reapply.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Overlay configuration data. The mandatory key bgp_type within the
    dict ca have value "internal" or "external". Structure is provided in the
    example.
  type: dict
  suboptions:
    name:
      description: Overlay Workflow Name
      type: str
      required: true
    fabric:
      description: Fabric Name
      type: str
      required: true
    vrf:
      description: VRF Name
      type: str
      required: true
    ipv4_address:
      description: IPv4 Resource Pool used for Loopbacks
      type: str
      required: true
    spine_leaf_asn:
      description: AS Number used for BGP configuration
      type: str
      required: true
    bgp_type:
      description: BGP Type used for Overlay configuration
      type: str
      choices:
      - internal
      - external
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create an overlay configuration using username and password
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-Overlay"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            ipv4_address: 'IP POOL'
            spine_leaf_asn: "65001"
            bgp_type: 'internal'

-   name: Reapply an overlay configuration using username and password
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: reapply
        data:
            name: "Test-Overlay"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"

-   name: Create an overlay configuration using token
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-Overlay"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            ipv4_address: 'IP POOL'
            spine_leaf_asn: "65001"
            bgp_type: 'internal'

-   name: Reapply an overlay configuration using token
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: reapply
        data:
            name: "Test-Overlay"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
```
