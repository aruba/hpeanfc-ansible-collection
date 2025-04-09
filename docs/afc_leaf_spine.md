# module: afc_leaf_spine

Description: This module is used to configure L3 or Subleaf leaf-spine configuration.

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
ls_type:
    description: >
        Type of leaf-spine configuration.
    type: str
    required: true
data:
    description: >
        Leaf spine configuration data according to the ls_type. Structure is provided in the example.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Configure L3 leaf-spine settings using username and password
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        ls_type: "l3"
        data:
            name: "Test-L3-LeafSpine"
            pool_ranges: "IP POOL"

-   name: Configure Subleaf leaf-spine settings using username and password
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        ls_type: "subleaf"
        data:
            name: "Test-Subleaf-LeafSpine"

-   name: Configure L3 leaf-spine settings using token
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        ls_type: "l3"
        data:
            name: "Test-L3-LeafSpine"
            pool_ranges: "IP POOL"

-   name: Configure Subleaf leaf-spine settings using token
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        ls_type: "subleaf"
        data:
            name: "Test-Subleaf-LeafSpine"
```
