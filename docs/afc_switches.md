# module: afc_switches

Description: This module performs defined action on the switches.

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
        Operation to be performed on the switch - One of : update, reconcile, reboot, save.
    type: str
    required: true
data:
    description: >
        Data used to act on switches. Structre is provided in the example.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Update switch data on AFC using username and password
    afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "update"
        data:
            switches: "10.10.10.15"
            name: "Update_Switch_Name"

-   name: Reconcile switch on AFC using username and password
    afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reconcile"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            Fabric:
                - "DC-Fabric"

-   name: Reboot switch through AFC using username and password
    afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reboot"
        data:
            - switches:
                - "10.10.10.15"
                - "10.10.10.16"
              boot_partition: 'active'
            - fabric:
                - "DC-Fabric"
              boot_partition: 'non-active'

-   name: Save configuraton on switches through AFC using username and password
    afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "save"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            Fabric:
                - "DC-Fabric"

-   name: Update switch data on AFC using token
    afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "update"
        data:
            switches: "10.10.10.15"
            name: "Update_Switch_Name"

-   name: Reconcile switch on AFC using token
    afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reconcile"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            Fabric:
                - "DC-Fabric"

-   name: Reboot switch through AFC using token
    afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reboot"
        data:
            - switches:
                - "10.10.10.15"
                - "10.10.10.16"
              boot_partition: 'active'
            - fabric:
                - "DC-Fabric"
              boot_partition: 'non-active'

-   name: Save configuraton on switches through AFC using token
    afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "save"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            Fabric:
                - "DC-Fabric"
```
