# module: afc_evpn

Description: This module is used to create and delete EVPN.

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
  description: Operation to be performed with the EVPN.
  type: str
  choices:
  - create
  - reapply
  required: true
data:
  description: VNI Data with system_mac_range, as_number, name_prefix, rt_type,
    vlans, vni_base and description.
  type: dict
  suboptions:
    fabric:
      description: Fabric Name
      type: str
      required: true
    vrf:
      description: VRF Name
      type: str
      required: true
    name:
      description: EVPN Workflow Name
      type: str
      required: true
    description:
      description: EVPN Workflow description
      type: str
      required: false
    system_mac_range:
      description: MAC Range used for Router MAC
      type: str
      required: true
    as_number:
      description: AS Number. Required based on selected rt_type.
      type: str
      required: true
    rt_type:
      description: Type of Route Target.
      type: str
      choices:
      - AUTO
      - ASN:VNI
      - ASN:VLAN
      - ASN:NN
      default: AUTO
      required: false
    vlans:
      description: VLANs to be mapped to EVPN
      type: str
      required: true
    vni_base:
      description: Used to combine with VLAN to form L2VNI
      type: str
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "Test-EVPN"
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Delete EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "Test-EVPN"

-   name: Reapply EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reapply"
        data:
            fabric: "Aruba-Fabric"

-   name: Create EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            name: "Test-EVPN"
            vrf: "Aruba-VRF"
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Delete EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "Test-EVPN"

-   name: Reapply EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reapply"
        data:
            fabric: "Aruba-Fabric"
```
