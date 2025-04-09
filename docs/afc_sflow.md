# module: afc_sflow

Description: This module creates or deletes a SFlow configuration in the specified fabric.

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
operation:
    description: >
        Operation to be performed on the SFlow configuration, create or delete.
    type: str
    required: true
sflow_name:
    description: >
        Name of the SFlow configuration to be created or deleted.
    type: str
    required: true
sflow_data:
    description: >
        SFlow configuration as per the example below. Strucutre is provided in the example.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Create a SFlow configuration using username and password
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        sflow_name: "Test-Sflow"
        sflow_data:
            enable_sflow: false
            polling_interval: 20
            sampling_rate: 20000
            source_namespace: "management"
            collectors:
                -   destination_port: 6343
                    destination_ip_address: "192.168.56.12"
            fabrics: "Test-Fabric"

-   name: Delete a SFlow configuration using username and password
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        sflow_name: "Test-Sflow"
        operation: "delete"

-   name: Create a SFlow configuration using token
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        sflow_name: "Test-Sflow"
        sflow_data:
            enable_sflow: false
            polling_interval: 20
            sampling_rate: 20000
            source_namespace: "management"
            collectors:
                -   destination_port: 6343
                    destination_ip_address: "192.168.56.12"
            fabrics: "Test-Fabric"

-   name: Delete a SFlow configuration using token
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        sflow_name: "Test-Sflow"
        operation: "delete"
```
