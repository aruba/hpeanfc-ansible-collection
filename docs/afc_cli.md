# module: afc_cli

Description: This module provides ability to run CLI commands.

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
data:
    description:
    - The input data to run the CLI commands on the designated targets. Structure is provided in the example.
    type: str
    required: true
```

##### EXAMPLES

```YAML
-   name: Run list of commands on switches using username and password
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            switches:
                - "10.10.10.14"
                - "10.10.10.15"
            commands:
                - "show arp"
                - "show bgp all summary"

-   name: Run list of commands on switches using the token
    arubanetworks.afc.afc_dhcp_relay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            switches:
                - "10.10.10.14"
                - "10.10.10.15"
            commands:
                - "show arp"
                - "show bgp all summary"
```
