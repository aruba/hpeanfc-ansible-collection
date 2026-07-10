# module: afc_snmp

Description: This module creates or deletes an SNMP configuration.

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
  description: Operation to be performed on an SNMP configuration, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: SNMP configuration in dictionary format as depicted in the example.
    Structure is provided in the example.
  type: dict
  suboptions:
    name:
      description: SNMP Workflow Name
      type: str
      required: true
    fabrics:
      description: List of fabrics
      type: list
      elements: str
      required: true
    enable:
      description: Enable configuration
      type: bool
      default: true
      required: false
    location:
      description: SNMP Location
      type: str
      required: false
    contact:
      description: SNMP contact
      type: str
      required: false
    community:
      description: SNMP community
      type: str
      required: false
    agent_port:
      description: SNMP Agent port
      type: int
      default: 161
      required: false
    trap_port:
      description: SNMP Trap port
      type: int
      required: false
    users:
      description: SNMPv3 user
      type: list
      elements: dict
      suboptions:
        name:
          description: Username
          type: str
          required: true
        level:
          description: User level
          type: str
          choices:
          - noauth
          - auth
          - priv
          required: true
        auth_type:
          description: User Authentication Type
          type: str
          choices:
          - SHA
          - MD5
          default: SHA
          required: false
        auth_pass:
          description: User Authentication Password
          type: str
          required: false
        priv_type:
          description: User Privacy Type
          type: str
          choices:
          - AES
          - DES
          default: AES
          required: false
        priv_pass:
          description: User Privacy Password
          type: str
          required: false
        context:
          description: SNMPv3 context
          type: str
          required: false
      required: false
    servers:
      description: SNMP servers
      type: list
      elements: dict
      suboptions:
        address:
          description: Server's IPv4 address
          type: str
          required: true
        community:
          description: SNMP Community
          type: str
          required: true
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create an SNMPv3 configuration using username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
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

-   name: Create an SNMPv2c configuration with Trap Server using username and
          password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
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
        operation: "create"
        data:
            name: "Test-SNMP"
            fabrics:
                - "Test-Fabric"
            enable: true
            location: "DC"
            contact: "admin"
            community: "private"

-   name: Create an SNMPv2c configuration only on some devices using
          username and password
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-SNMP"
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
        data:
            name: "Test-SNMP"
        operation: "delete"

-   name: Create an SNMPv3 configuration using token
    arubanetworks.afc.afc_snmp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-SNMP"
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
        operation: "create"
        data:
            name: "Test-SNMP"
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
        operation: "create"
        data:
            name: "Test-SNMP"
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
        operation: "create"
        data:
            name: "Test-SNMP"
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
        data:
            name: "Test-SNMP"
        operation: "delete"
```
