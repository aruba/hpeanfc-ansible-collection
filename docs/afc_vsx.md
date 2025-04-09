# module: afc_vsx

Description: This module creates or deletes a VSX configuration in the specified fabric.

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
fabric_name:
    description: >
        Name of the Fabric where the VSX configuration will be created or deleted from.
    type: str
    required: true
operation:
    description: >
        Operation to be performed on the VSX, create delete or reapply.
    type: str
    required: true
vsx_name:
    description: >
        Name of the VSX Configuration.
    type: str
    required: true
vsx_data:
    description: >
        VSX configuration data as specified in the example below.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Create VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "create"
        vsx_name: "Test-VSX"
        vsx_data:
            system_mac_range: "MAC POOL"
            keepalive_ip_pool_range: "IP POOL"
            keep_alive_interface_mode: "loopback"

-   name: Reapply VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vsx_name: "Test-VSX"
        operation: "reapply"

-   name: Delete VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vsx_name: "Test-VSX"
        operation: "delete"

-   name: Create VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "create"
        vsx_name: "Test-VSX"
        vsx_data:
            system_mac_range: "MAC POOL"
            keepalive_ip_pool_range: "IP POOL"
            keep_alive_interface_mode: "routed"

-   name: Reapply VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vsx_name: "Test-VSX"
        operation: "reapply"

-   name: Delete VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vsx_name: "Test-VSX"
        operation: "delete"
```
