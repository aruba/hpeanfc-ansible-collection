# module: afc_dss

Description: This module creates or deletes a DSS objects.

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
dss_object_name:
    description: >
        Name of the object that will be created or deleted from.
    type: str
    required: true
dss_object_type:
    description: >
        Type of the dss object. Options policy, endpoint_group, rule, qualifier, vnic_move.
    type: str
    required: true
dss_object_data:
    description: >
        Object specific data for policy, endpoint_group, rule, qualifier, vnic_move.
    type: dict
    required: true
operation:
    description: >
        Operation to be performed on the DSS configuration, create or delete.
    type: str
    required: true
```

##### EXAMPLES

```YAML
-   name: Create policy using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        dss_object_data:
            policy_subtype: "firewall"
            priority: 10
            rules:
                - "test_rule"
            enforcers:
                -   fabric: "Test-Fabric"
                    vrf: "Test-VRF"
                    network: "VLAN251"
                    enforcer_type: "network"
                    direction: "egress"
                    pdt_type: "leaf"
            object_type: "policy"
        operation: "create"

-   name: Delete policy using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        operation: "delete"

-   name: Create rule using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        dss_object_data:
            action: "drop"
            source_endpoint_groups:
                - "test_eg"
            destination_endpoint_groups:
                - "test_eg"
            service_qualifiers:
                - "icmp"
                - "bgp"
                - "test_sq"
        operation: "create"

-   name: Delete rule using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        operation: "delete"

-   name: Create endpoint group using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        dss_object_data:
            type: "layer3"
            endpoints:
                -   vm_name: "Test-Fabric"
                    vnic_name: "Network adapter 1"
        operation: "create"

-   name: Delete endpoint group using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        operation: "delete"

-   name: Create qualifier using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        dss_object_data:
            protocol_identifier:
                -   src_port: "32"
                    dst_port: "32"
                    ip_protocol: "tcp"
            qualifier_type: "layer3"
        operation: "create"

-   name: Delete qualifier using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        operation: "delete"

-   name: Create policy using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        dss_object_data:
            policy_subtype: "firewall"
            priority: 10
            rules:
                - "test_rule"
            enforcers:
                -   fabric: "Test-Fabric"
                    vrf: "Test-VRF"
                    network: "VLAN251"
                    enforcer_type: "network"
                    direction: "egress"
                    pdt_type: "leaf"
            object_type: "policy"
        operation: "create"

-   name: Delete policy using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_policy"
        dss_object_type: "policy"
        operation: "delete"

-   name: Create rule using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        dss_object_data:
            action: "drop"
            source_endpoint_groups:
                - "test_eg"
            destination_endpoint_groups:
                - "test_eg"
            service_qualifiers:
                - "icmp"
                - "bgp"
                - "test_sq"
        operation: "create"

-   name: Delete rule using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_rule"
        dss_object_type: "rule"
        operation: "delete"

-   name: Create endpoint group using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        dss_object_data:
            type: "layer3"
            endpoints:
                -   vm_name: "Test-Fabric"
                    vnic_name: "Network adapter 1"
        operation: "create"

-   name: Delete endpoint group using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_eg"
        dss_object_type: "endpoint_group"
        operation: "delete"

-   name: Create qualifier using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        dss_object_data:
            protocol_identifier:
                -   src_port: "32"
                    dst_port: "32"
                    ip_protocol: "tcp"
            qualifier_type: "layer3"
        operation: "create"

-   name: Delete qualifier using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        dss_object_name: "test_sq"
        dss_object_type: "qualifier"
        operation: "delete"
```
