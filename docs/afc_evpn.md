# module: afc_evpn

Description: This module is used to create and delete EVPN.

##### ARGUMENTS

```YAML
afc_ip:
    description: >
        IP address of the Aruba Fabric Composer.
    type: str
    required: true
afc_username:
    description:
    - User account having write permission on the Aruba Fabric Composer
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
operation:
    description: >
        Operation to be performed with the EVPN, create, delete or reapply.
    type: str
    required: true
vni_data:
    description: >
        VNI Data with system_mac_range, as_number, name_prefix, rt_type, vlans, vni_base and description.
        The values as_number, vlans and the vni_base, though integers need to be represented as string.
        Structure is provided in the example. Not needed for reapply
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "create"
        vni_data:
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            name_prefix: "Test-EVPN"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Delete EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "delete"
        vni_data:
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            name_prefix: "Test-EVPN"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Reapply EVPN using username and password
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "reapply"

-   name: Create EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "create"
        vni_data:
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            name_prefix: "Test-EVPN"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Delete EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "delete"
        vni_data:
            system_mac_range: "MAC Range Name"
            as_number: "65000"
            name_prefix: "Test-EVPN"
            rt_type: "ASN:VNI"
            vlans: "250"
            vni_base: "10000"
            description: "Test EVPN"

-   name: Reapply EVPN using token
    arubanetworks.afc.afc_evpn:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "reapply"
```
