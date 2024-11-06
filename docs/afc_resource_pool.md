# module: afc_resource_pool

Description: This module creates or deletes a Resource Pool configuration.

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
resource_pool_name:
    description: >
        Name of the resource pool.
    type: str
    required: true
resource_pool_data:
    description: >
        Resource pool data containing type and pool_ranges
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Create resource pool using username and password
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        resource_pool_name: "IP POOL"
        operation: "create"
        resource_pool_data:
            type: "IPv4"
            pool_ranges: "10.10.20.0/24"

-   name: Delete resource pool using username and password
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        resource_pool_name: "IP POOL"
        operation: "delete"

-   name: Create resource pool using token
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        resource_pool_name: "IP POOL"
        operation: "create"
        resource_pool_data:
            type: "IPv4"
            pool_ranges: "10.10.20.0/24"

-   name: Delete resource pool using token
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        resource_pool_name: "IP POOL"
        operation: "delete"
```
