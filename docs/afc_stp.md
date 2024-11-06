# module: afc_stp

Description: This module creates or deletes an STP configuration.

##### ARGUMENTS

```YAML
afc_ip:
    description: >
        IP address of the Aruba Fabric Composer.
    type: str
    required: true
afc_username:
    description:
    - User account having permission to create VRF on the Aruba Fabric Composer
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
        Operation to be performed on the STP configuration, create or delete.
    type: str
    required: true
stp_name:
    description: >
        Name of the STP configuration to be created or deleted.
    type: str
    required: true
stp_data:
    description: >
        STP data as depicted in the example.
    type: dict
    required: false
```

##### EXAMPLES

```YAML
-   name: Create STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        stp_name: "Test-STP"
        operation: "create"
        stp_data:
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        stp_name: "Test-STP"
        operation: "delete"

-   name: Create STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        stp_name: "Test-STP"
        operation: "create"
        stp_data:
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        stp_name: "Test-STP"
        operation: "delete"
```
