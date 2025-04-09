# module: afc_dns

Description: This module creates or deletes a DNS Entry in the specified fabric.

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
    Operation to be performed on the VRF, create or delete.
  type: str
  required: true
dns_name:
  description: >
    Name of the DNS entry to be created.
  type: str
  required: true
dns_data:
  description: >
    Dictionary of the mandatory actions as depicted in the example. Required for create and not required for delete operations.
    Structure is provided in the example.
  type: dict
  required: false
```

##### EXAMPLES

```YAML
-   name: Create DNS Entry using username and password
    arubanetworks.afc.afc_dns:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        dns_name: "Test-DNS"
        dns_data:
            fabrics:
              - "Test-Fabric"
            domain_name: "example.com"
            name_servers:
              - "10.10.20.1"

-   name: Delete DNS Entry using username and password
    arubanetworks.afc.afc_dns:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        dns_name: "Test-DNS"

-   name: Create DNS Entry using token
    arubanetworks.afc.afc_dns:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        dns_name: "Test-DNS"
        dns_data:
            fabrics:
              - "Test-Fabric"
            domain_name: "example.com"
            name_servers:
              - "10.10.20.1"

-   name: Delete DNS Entry using token
    arubanetworks.afc.afc_dns:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        dns_name: "Test-DNS"
```
