# module: afc_dns

Description: This module creates or deletes a DNS Entry in the specified fabric.

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
  description: Operation to be performed on the DNS entry, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Dictionary of the mandatory actions as depicted in the example.
  type: dict
  required: true
  suboptions:
    name:
      description: DHCP Relay Config name
      type: str
      required: true
    description:
      description: DHCP Relay Config description
      type: str
      required: false
    domain_name:
      description: Domain Name to be used
      type: str
      required: false
    domain_list:
      description: List of Domains Names. Not required if "domain_name" is used
      type: list
      elements: str
      required: false
    name_servers:
      description: List of DNS Servers
      type: list
      elements: str
      required: true
    fabrics:
      description: List of Fabrics
      type: list
      elements: str
      required: false
    switches:
      description: List of Switches
      type: list
      elements: str
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
        data:
            name: "Test-DNS"
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
        data:
            name: "Test-DNS"

-   name: Create DNS Entry using token
    arubanetworks.afc.afc_dns:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-DNS"
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
        data:
            name: "Test-DNS"
```
