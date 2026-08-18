# module: afc_aaa

Description: This module creates or deletes an AAA configuration

##### ARGUMENTS

```YAML
afc_ip:
  description:
  - IP address of the HPE ANW Fabric Composer
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
  description:
  - Operation to be performed on the AAA configuration, create or delete
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: The radius configuration data for create operation. Structure is
    provided in the example
  type: dict
  suboptions:
    name:
      description: Radius Configuration name
      type: str
      required: true
    description:
      description: Radius Configuration description
      type: str
      required: true
    config:
      description: Radius configuration
      type: dict
      required: true
      suboptions:
        name:
          description: Radius Config name
          type: str
          required: true
        secret:
          description: Radius secret
          type: str
          required: true
        server:
          description: Radius Server IP Address
          type: str
          required: true
        port:
          description: Radius Port
          type: int
          required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create AAA Radius config using username and password
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Radius-Test"
            config:
                secret: "Test"
                server: "192.16.56.12"
                port: 1812


-   name: Delete AAA Radius config using username and password
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Radius-Test"

-   name: Create AAA Radius config using token
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Radius-Test"
            config:
                secret: "Test"
                server: "192.16.56.12"
                port: 1812

-   name: Delete AAA Radius config using token
    arubanetworks.afc.afc_aaa:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Radius-Test"
```
