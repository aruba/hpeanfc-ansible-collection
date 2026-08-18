# module: afc_dhcp_relay

Description: This module creates or deletes a DHCP Relay configuration in the fabric.

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
  description: Operation to be performed on the DHCP Relay configuration, create
    or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Dictionary containing mandatory details to create a DHCP relay.
    Required for create and not required for delete. Structure is provided in
    the example.
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
    vlans:
      description: Set or range of VLANs
      type: str
      required: false
    gateway_address:
      description: BOOTP-Gateway Address
      type: str
      required: false
    ipv4_dhcp_server_addresses:
      description: List of DHCP Servers IPv4 Addresses
      type: list
      elements: str
      required: false
    ipv6_dhcp_server_addresses:
      description: List of DHCP Servers IPv6 Addresses
      type: list
      elements: str
      required: false
    ipv6_dhcp_mcast_server_addresses:
      description: List of DHCP Servers IPv6 MCAST Addresses
      type: list
      elements: str
      required: false
    v4relay_option82_policy:
      description: Specifies the forwarding policy of DHCP-Relay Option 82
      type: str
      choices:
      - replace
      - drop
      - keep
      required: false
    v4relay_option82_validation:
      description: Set true to validate server response packets and set it to
        false otherwise. This configuration is disabled by default
      type: bool
      required: false
    v4relay_source_interface:
      description: Set true to enable DHCP-Relay to use the configured source-interface
        and include suboption-5 and suboption-11 in the relay option 82. This
        configuration is disabled by default
      type: bool
      required: false
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
-   name: Create DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-DHCP_Relay"
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        name: "Test-DHCP_Relay"
        operation: "delete"

-   name: Create DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-DHCP_Relay"
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        name: "Test-DHCP_Relay"
        operation: "delete"
```
