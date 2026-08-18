# module: afc_fabric

Description: This module is used to create, delete a fabric or assign multiple switches to the specified fabric along with role.

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
  description: Operation to be performed with the Fabric.
  type: str
  choices:
  - create
  - assign
  - delete
  required: true
data:
  description: Device assignment or Fabric Data.
  type: dict
  required: true
  suboptions:
    name:
      description: Fabric Name
      type: str
      required: true
    timezone:
      description: Timezone
      type: str
      required: false
    fabric_class:
      description: Class of fabric to discover.
      type: str
      choices:
      - data
      - management
      default: data
      required: false
    roles:
      description: Roles to be assigned on a per device basis The key must be
        an ipv4 address or and IPv4 range and the role must be one of the following
        values ["spine", "leaf", "border_leaf", "sub_leaf"]
      type: dict
      required: false
```

##### EXAMPLES

```YAML
-   name: Create Fabric using usename and password
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Aruba-Fabric"
            timezone: "Europe/London"

-   name: Delete Fabric using usename and password
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Aruba-Fabric"

-   name: Assign multiple switches to the Fabric and assign role using usename
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "assign"
        data:
            fabric: "Aruba-Fabric"
            roles:
                10.10.10.11: "border_leaf"
                10.10.10.12: "border_leaf"
                10.10.10.13: "spine"
                10.10.10.14: "spine"
                10.10.10.15: "leaf"
                10.10.10.16: "leaf"
                10.10.10.17: "subleaf"

-   name: Create Fabric using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Aruba-Fabric"
            timezone: "Europe/London"

-   name: Delete Fabric using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Aruba-Fabric"

-   name: Assign multiple switches to the Fabric and assign role using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "assign"
        data:
            fabric: "Aruba-Fabric"
            roles:
                10.10.10.11: "border_leaf"
                10.10.10.12: "border_leaf"
                10.10.10.13: "spine"
                10.10.10.14: "spine"
                10.10.10.15: "leaf"
                10.10.10.16: "leaf"
                10.10.10.17: "subleaf"
```
