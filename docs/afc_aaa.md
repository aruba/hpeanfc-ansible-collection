# module: afc_aaa

Description: This module provides ability to configure AAA.

##### ARGUMENTS

```YAML
afc_ip:
    description:
    - IP address of the Aruba Fabric Composer
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
    description:
    - Operation to be performed on the AAA configuration, create or delete
    type: str
    required: true
radius_name:
    description:
    - Name of the Radius configuration to be created or deleted
    type: str
    required: true
radius_data:
    description:
    - The readius configuration data for create operation. Structure is provided in the example
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create AAA Radius config using username and password
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        radius_name: "Radius-Test"
        radius_data:
            config:
                secret: "Test"
                server: "192.16.56.12"
                port: 1812
        operation: "create"

-   name: Delete AAA Radius config using username and password
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        radius_name: "Radius-Test"
        operation: "delete"

-   name: Create AAA Radius config using token
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        radius_name: "Radius-Test"
        radius_data:
            config:
                secret: "Test"
                server: "192.16.56.12"
                port: 1812
        operation: "create"

-   name: Delete AAA Radius config using token
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        radius_name: "Radius-Test"
        operation: "delete"
```
