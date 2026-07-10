# module: afc_leaf_spine

Description: This module is used to configure Leaf-Spine relationship.

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
data:
  description: Leaf spine configuration data according to the type. Structure
    is provided in the example.
  type: dict
  suboptions:
    fabric:
      description: Fabric Name
      type: str
      required: true
    name:
      description: IP Interface Name
      type: str
      required: true
    type:
      description: Type of Leaf and Spine topology.
      type: str
      choices:
      - l3
      - subleaf
      required: true
    pool_ranges:
      description: L3LS specific. IPv4 Resource Pool to configure ROP.
      type: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Configure L3 leaf-spine settings using username and password
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            fabric: "Aruba-Fabric"
            type: "l3"
            name: "Test-L3-LeafSpine"
            pool_ranges: "IP POOL"

-   name: Configure Subleaf leaf-spine settings using username and password
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            fabric: "Aruba-Fabric"
            type: "subleaf"
            name: "Test-Subleaf-LeafSpine"

-   name: Configure L3 leaf-spine settings using token
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            fabric: "Aruba-Fabric"
            type: "l3"
            name: "Test-L3-LeafSpine"
            pool_ranges: "IP POOL"

-   name: Configure Subleaf leaf-spine settings using token
    arubanetworks.afc.afc_leaf_spine:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            fabric: "Aruba-Fabric"
            type: "subleaf"
            name: "Test-Subleaf-LeafSpine"
```
