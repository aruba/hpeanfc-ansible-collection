# module: afc_discovery

Description: This module discovers the switches matching the input IP addresses.

##### ARGUMENTS

```YAML
afc_ip:
    description: >
        IP address of the HPE ANW Fabric Composer.
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
    description: >
        Auth token from the create session playbook.
    type: str
    required: false
discovery_data:
    description: >
        Discovery data containing default admin credentials of the switch and the password for afc_admin user.
    type: dict
    required: true
devices_list:
    description: >
        List of IP address of the devices that need to be discovered.
    type: list
    required: true
```

##### EXAMPLES

```YAML
-   name: Run discovery of the switches through AFC using username and password
    afc_discovery:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        discovery_data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
        devices_list:
            - "10.10.10.11"
            - "10.10.10.12"

-   name: Run discovery of the switches through AFC using token
    afc_discovery:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        discovery_data:
            admin_passwd: "switch_admin_password"
            afc_admin_passwd: "afc_admin_password"
        devices_list:
            - "10.10.10.11"
            - "10.10.10.12"
```
