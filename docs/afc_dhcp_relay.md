# module: afc_dhcp_relay

Description: This module creates or deletes a DHCP Relay configuration in the specified fabric.

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
        Operation to be performed on the DHCP Relay configuration, create or delete.
    type: str
    required: true
dhcp_relay_name:
    description: >
        Name of the DHCP Relay configuration to be created or deleted.
    type: str
    required: true
dhcp_relay_data:
    description: >
        Dictionary containing mandatory details to create a DHCP relay. Required for create and not required for delete.
        Structure is provided in the example.
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dhcp_relay_name: "Test-DHCP_Relay"
        operation: "create"
        dhcp_relay_data:
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv6_dhcp_mcast_server_addresses: []
            ipv6_dhcp_server_addresses: []
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dhcp_relay_name: "Test-DHCP_Relay"
        operation: "delete"

-   name: Create DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dhcp_relay_name: "Test-DHCP_Relay"
        operation: "create"
        dhcp_relay_data:
            fabrics:
                - "Test-Fabric"
            vlans: "251"
            ipv6_dhcp_mcast_server_addresses: []
            ipv6_dhcp_server_addresses: []
            ipv4_dhcp_server_addresses:
                - "1.2.3.4"

-   name: Delete DHCP Relay configuration using token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dhcp_relay_name: "Test-DHCP_Relay"
        operation: "delete"
```
