# module: afc_resource_pool

Description: This module create or delete the resource pool.

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
  description: Create or Delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Resource pool data containing name, type and pool_ranges. Structure
    is provided in the example.
  type: dict
  suboptions:
    name:
      description: Resource Pool Name
      type: str
      required: true
    type:
      description: Resource Pool type
      type: str
      choices:
      - IPv4
      - MAC
      required: false
    pool_ranges:
      description: Pool Range.
      type: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create IPv4 resource pool using username and password
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "IP POOL"
            type: "IPv4"
            pool_ranges: "10.10.20.0/24"

-   name: Create MAC resource pool using username and password
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "MAC POOL"
            type: "MAC"
            pool_ranges: "00:00:00:00:00:01-00:00:00:00:00:FF"

-   name: Delete resource pool using username and password
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "IP POOL"

-   name: Create resource pool using token
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "IP POOL"
            type: "IPv4"
            pool_ranges: "10.10.20.0/24"

-   name: Delete resource pool using token
    arubanetworks.afc.afc_resource_pool:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "IP POOL"
```
