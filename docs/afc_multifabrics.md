# module: afc_multifabrics

Description: This module is used to configure Multi-Fabrics.

##### ARGUMENTS

```YAML
afc_ip:
  description: IP address of HPE ANW Fabric Composer.
  type: str
  required: true
afc_username:
  description: User account having permission to create MF on HPE ANW Fabric Composer
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
  description: Operation to execute - Create.
  type: str
  choices:
  - create
  required: true
data:
  description: Multi-Fabrics data containing information.
  type: dict
  suboptions:
    name:
      description: EVPN Workflow Name
      type: str
      required: true
    local_fabric:
      description: Name of the local Fabric
      type: str
      required: true
    border_leader:
      description: Name or IPv4 Address of the Border Leader. In case of VSX just
        provide the Name or IPv4 Address of one of the members.
      type: str
      required: true
    l3_ebgp_borders:
      description: L3 eBGP border switch(es)
      type: list
      elements: str
      required: false
    bgp_auth_password:
      description: Set password for bgp neighbor
      type: str
      required: false
    uplink_to_uplink:
      description: Enable or Disable uplink to uplink.
      type: bool
      required: false
    remote_fabrics:
      description: Information related to the remote Fabric.
      type: list
      elements: dict
      required: true
      suboptions:
        fabric:
          description: Name of the remote Fabric
          type: str
          required: true
        border_leader:
          description: Name or IPv4 Address of the Border Leader. In case of VSX
            just provide the Name or IPv4 Address of one of the members.
          type: str
          required: true
        peering_ip:
          description: IP address for BGP neighbor peering
          type: str
          required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Configure L3LS settings using username and password
    arubanetworks.afc.afc_multifabrics:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "MF-ArubaFabric"
            local_fabric: "Aruba-Fabric"
            border_leader: "10.10.10.20"
            remote_fabrics:
                - fabric: "Aruba-Fabric2"
                  border_leader: "10.20.20.20"
                  peering_ip: "loopback0"

-   name: Configure L3LS settings using token
    arubanetworks.afc.afc_multifabrics:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "MF-ArubaFabric"
            local_fabric: "Aruba-Fabric"
            border_leader: "10.10.10.20"
            remote_fabrics:
                - fabric: "Aruba-Fabric2"
                  border_leader: "10.20.20.20"
                  peering_ip: "loopback0"
```
