# module: afc_leaf_spine

Description: This module is used to create and delete Switch Virtual Interface or IP Interface.

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
l3ls_data:
    description: >
        L3LS data containing name and the pool_ranges.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Configure L3LS settings using username and password
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        l3ls_data:
            name: "Test-L3LS"
            pool_ranges: "IP POOL"

-   name: Configure L3LS settings using token
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        l3ls_data:
            name: "Test-L3LS"
            pool_ranges: "IP POOL"
```
