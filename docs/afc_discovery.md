# module: afc_discovery

Description: This module discovers the switches matching the input IP addresses.

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
data:
  description: List of IP addresses of the devices that need to be discovered,
    with credentials required for discovery.
  type: dict
  required: true
  suboptions:
    switches:
      description: List of IP Addresses or ranges to discover
      type: list
      elements: str
      required: true
    admin_passwd:
      description: Admin password to connect on switches.
      type: str
      required: true
    afc_admin_passwd:
      description: AFC user password to be created on switches
      type: str
      required: true
    service_account_user:
      description: AFC user to be created on switches.
      type: str
      default: admin
      required: false
```

##### EXAMPLES

```YAML
-   name: Run discovery of the switches through AFC using username and password
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"

-   name: Run discovery of the switches through AFC using username and password
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11-10.10.10.20"
                - "10.10.10.22"

-   name: Run discovery of the switches through AFC using token
    arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
            switches:
                - "10.10.10.11"
                - "10.10.10.12"
```
