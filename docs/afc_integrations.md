# module: afc_integrations

Description: This module creates integration with Pensando PSM or VMWare.

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
        Operation to be performed on the integration configuration, create or delete.
    type: str
    required: true
integration_type:
    description: >
        Type of integration - Can be either vmware_vsphere or pensando_psm.
    type: str
    required: true
integration_data:
    description: >
        integration configuration data. Structure is provided in the example.
    type: dict
    required: true
```

##### EXAMPLES

```YAML
-   name: Create an integration with VMware vSphere using username and password
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        integration_type: "vmware_vsphere"
        integration_data:
            name: "vSphere"
            host: "10.10.10.11"
            username: "administrator@vsphere.local"
            password: "password"
            enabled: True
            verify_ssl: False
            auto_discovery: True
            vlan_provisioning: True
            pvlan_provisioning: True
            downlink_vlan_range: "1-4094"
            vlan_range: "1-4094"
            pvlan_range: "1-4094"
            use_cdp: False
            downlink_vlan_provisioning: False
            storage_optimization: False
            endpoint_group_provisioning: True

-   name: Create an integration with Pensando PSM using username and password
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        integration_type: "pensando_psm"
        integration_data:
            name: "PSM"
            username: "admin"
            password: "password"
            fabrics:
                - "FABRIC"
            host: "10.10.10.12"

-   name: Create an integration with VMware vSphere using token
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        integration_type: "vmware_vsphere"
        integration_data:
            name: "vSphere"
            host: "10.10.10.11"
            username: "administrator@vsphere.local"
            password: "password"
            enabled: True
            verify_ssl: False
            auto_discovery: True
            vlan_provisioning: True
            pvlan_provisioning: True
            downlink_vlan_range: "1-4094"
            vlan_range: "1-4094"
            pvlan_range: "1-4094"
            use_cdp: False
            downlink_vlan_provisioning: False
            storage_optimization: False
            endpoint_group_provisioning: True

-   name: Create an integration with Pensando PSM using token
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        integration_type: "pensando_psm"
        integration_data:
            name: "PSM"
            username: "admin"
            password: "password"
            fabrics:
                - "FABRIC"
            host: "10.10.10.12"
```
