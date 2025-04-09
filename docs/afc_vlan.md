# module: afc_vlan

Description: This module creates or deletes a VLAN in the specified fabric.

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
operation:
    description: >
        Operation to be performed with the VLAN, create or delete
    type: str
    required: true
fabric_name:
    description: >
        Name of the Fabric on which VLAN to be created or deleted from
    type: str
    required: true
vrf_name:
    description: >
        Name of the VRF to which VLAN belongs
    type: str
    required: true
vlan_id:
    description: >
        ID of the VLAN to be created or deleted.
    type: int
    required: true
```

##### EXAMPLES

```YAML
-   name: Create VLAN in Aruba Fabric Composer using username and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: "create"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Test-VRF"
        vlan_id: 1008

-   name: Delete VLAN in Aruba Fabric Composer using username and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: "delete"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Test-VRF"
        vlan_id: 1008

-   name: Create VLAN in Aruba Fabric Composer using token
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Test-VRF"
        vlan_id: 1008

-   name: Delete VLAN in Aruba Fabric Composer using token
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Test-VRF"
        vlan_id: 1008
```
