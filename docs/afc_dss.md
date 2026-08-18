# module: afc_dss

Description: This module creates a DSS configuration item.

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
  description: Operation to be performed on the DSS configuration, create or update
    (only network).
  type: str
  choices:
  - create
  - delete
  - update
  required: true
data:
  description: Object specific data for policy, endpoint_group, rule, qualifier
    or network. Structure is provided in the example.
  type: dict
  suboptions:
    name:
      description: DSS Object Name
      type: str
      required: true
    type:
      description: DSS Object type
      type: str
      choices:
      - network
      - qualifier
      - endpoint_group
      - rule
      - policy
      required: true
    policy_subtype:
      description: DSS Policy specific. Subtype
      type: str
      choices:
      - firewall
      - layer3
      - layer2
      required: true
    enforcers:
      description: DSS Policy specific. Policy Enforcers
      type: list
      elements: dict
      required: false
      suboptions:
        direction:
          description: Apply the policy in this direction on the enforcer
          type: str
          choices:
          - ingress
          - egress
          required: true
        fabric:
          description: Fabric on which to apply the Policy
          type: str
          required: true
        enforcer_type:
          description: Type of the enforcer.
          type: str
          choices:
          - network
          - vrf
          required: true
        vrf:
          description: VRF on which to apply the Policy
          type: str
          required: true
        network:
          description: Network on which to apply the Policy
          type: str
          required: false
    priority:
      description: DSS Policy specific. Priority is used to determine ordering
        of Policies applied to the same direction of a specific Enforcer
      type: int
      required: true
    rules:
      description: DSS Policy specific. List of rules to be used in that policy.
        Rules order will be used.
      type: list
      elements: str
      required: false
    action:
      description: DSS Rule specific. Action to be used on that Rule
      type: str
      choices:
      - allow
      - drop
      - reject
      required: false
    source_endpoint_groups:
      description: DSS Rule specific. List of sources
      type: list
      elements: str
      required: false
    destination_endpoint_groups:
      description: DSS Rule specific. List of destination
      type: list
      elements: str
      required: false
    service_qualifiers:
      description: DSS Rule specific. List of qualifiers
      type: list
      elements: str
      required: false
    eg_type:
      description: Endpoint Group specific. Type of Endpoint Group
      type: str
      choices:
      - layer3
      - layer2
      - firewall
      required: false
    endpoints:
      description: DSS Endpoint Group specific. List of Endpoint Groups
      type: list
      elements: dict
      required: false
      suboptions:
        vm_name:
          description: Name of the VM
          type: str
          required: false
        vnic_name:
          description: Name of the vNic
          type: str
          required: false
        vmkernel_adapter_name:
          description: Name of the VMK
          type: str
          required: false
        vm_tag:
          description: VMs' tag
          type: str
          required: false
    protocol_identifier:
      description: DSS Qualifier specific. List of Qualifiers
      type: list
      elements: dict
      required: false
      suboptions:
        src_port:
          description: Source Port
          type: str
          required: false
        dst_port:
          description: Destination Port
          type: str
          required: false
        ip_protocol:
          description: IP Protocol
          type: str
          required: false
    vlan_id:
      description: DSS Network specific. VLAN ID to be mapped to the Network
      type: str
      required: true
    service_bypass:
      description: DSS Network specific. Enable Service Bypass on this Network
      type: str
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create policy using username and password using Network
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_policy"
            type: "policy"
            policy_subtype: "firewall"
            enforcers:
                - direction: egress
                  fabric: Aruba-Fabric
                  enforcer_type: vrf
                  vrf: Aruba-VRF
                  network: VLAN100
            priority: 1
            rules:
                - DropICMP
                - AllowAll
        operation: "create"

-   name: Create policy using username and password using VRF
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_policy"
            type: "policy"
            policy_subtype: "firewall"
            enforcers:
                - direction: egress
                  enforcer_type: vrf
                  fabric: Aruba-Fabric
                  vrf: Aruba-VRF
            priority: 1
            rules:
                - DropICMP
                - AllowAll
        operation: "create"

-   name: Delete policy using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "test_policy"
            type: "policy"

-   name: Create rule using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_rule"
            type: "rule"
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
        operation: "delete"
        data:
            name: "test_rule"
            type: "rule"

-   name: Create endpoint group using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_eg"
            type: "endpoint_group"
            eg_type: "layer3"
            endpoints:
                -   vm_name: "VM1"
                    vnic_name: "Network adapter 1"
        operation: "create"

-   name: Delete endpoint group using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "test_eg"
            type: "endpoint_group"

-   name: Create qualifier using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_sq"
            type: "qualifier"
            qualifier_type: "layer3"
            protocol_identifier:
                -   src_port: "32"
                    dst_port: "32"
                    ip_protocol: "tcp"
        operation: "create"

-   name: Delete qualifier using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "test_sq"
            type: "qualifier"

-   name: Create network using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            vlan_id: 100
            service_bypass: true
        operation: "create"

-   name: Update network using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            vlan_id: 1080
            service_bypass: true
        operation: "update"

-   name: Delete network using username and password
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
        operation: "delete"

-   name: Create policy using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_policy"
            type: "policy"
            policy_subtype: "firewall"
            enforcers:
                - direction: egress
                  enforcer_type: vrf
                  fabric: Aruba-Fabric
                  vrf: Aruba-VRF
            priority: 1
            rules:
                - DropICMP
                - AllowAll
        operation: "create"
        operation: "create"

-   name: Delete policy using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "test_policy"
            type: "policy"

-   name: Create rule using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_rule"
            type: "rule"
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
        data:
            name: "test_rule"
            type: "rule"
        operation: "delete"

-   name: Create endpoint group using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_eg"
            type: "endpoint_group"
            eg_type: "layer3"
            endpoints:
                -   vm_name: "VM1"
                    vnic_name: "Network adapter 1"
        operation: "create"

-   name: Delete endpoint group using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "test_eg"
            type: "endpoint_group"

-   name: Create qualifier using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_sq"
            type: "qualifier"
            qualifier_type: "layer3"
            protocol_identifier:
                -   src_port: "32"
                    dst_port: "32"
                    ip_protocol: "tcp"
        operation: "create"

-   name: Delete qualifier using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "test_sq"
            type: "qualifier"

-   name: Create network using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            vlan_id: 1080
            service_bypass: true
        operation: "update"

-   name: Update network using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            vlan_id: 1080
            service_bypass: true
        operation: "update"

-   name: Delete network using token
    arubanetworks.afc.afc_dss:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "test_network"
            type: "network"
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
        operation: "delete"
```
