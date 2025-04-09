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
        Structure is provided in the example.
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create an SNMPv3 configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "snmp_admin"
                    auth_type: "SHA"
                    auth_pass: "password"
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration with Trap Server using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Create an SNMPv2c configuration only on some devices using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Delete an SNMP configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        snmp_name: "Test-SNMP"
        operation: "delete"

-   name: Create an SNMPv3 configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            users:
                -   level: "auth"
                    name: "snmp_admin"
                    auth_type: "SHA"
                    auth_pass: "password"
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration with Trap Server using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"
            agent_port: 161
            trap_port: 23
            servers:
                -   address: "1.2.3.4"
                    community: "private"

-   name: Create an SNMPv2c configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            fabrics: 
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Create an SNMPv2c configuration only on some devices using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "create"
        snmp_data:
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Delete an SNMP configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        snmp_name: "Test-SNMP"
        operation: "delete"
```
