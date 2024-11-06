# module: afc_snmp

Description: This module creates or deletes an SNMP configuration in the specified fabric.

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
operation:
    description: >
        Operation to be performed on an SNMP configuration, create or delete.
    type: str
    required: true
snmp_name:
    description: >
        Name of the SNMP Configuration to be created or deleted.
    type: str
    required: true
snmp_data:
    description: >
        SNMP configuration in dictionary format as depicted in the example. Required for create and not required for delete.
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create an SNMP configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: "Test-Fabric"
            enable: true
            location: "eee"
            contact: "eee"
            community: "eee"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "eee"
                    auth_type: "SHA"
                    auth_pass: "eeeeeeeeee"
            servers:
                -   address: "1.2.3.4"
                    community: "eeeee"

-   name: Delete an SNMP configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "delete"

-   name: Create an SNMP configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: "Test-Fabric"
            enable: true
            location: "eee"
            contact: "eee"
            community: "eee"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "eee"
                    auth_type: "SHA"
                    auth_pass: "eeeeeeeeee"
            servers:
                -   address: "1.2.3.4"
                    community: "eeeee"

-   name: Delete an SNMP configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "delete"
```
