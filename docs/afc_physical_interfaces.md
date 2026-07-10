# module: afc_physical_interfaces

Description: This module is used to configure physical ports.

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
data:
  description: Port configuration data. Structure is provided in the example.
  type: list
  elements: dict
  suboptions:
    switch:
      description: Switch IP Address
      type: str
      required: true
    ports_config:
      description: List of physical ports on that switch
      type: list
      elements: dict
      required: true
      suboptions:
        name:
          description: Port ID
          type: str
          required: true
        ungrouped_vlans:
          description: set of VLANs to be configured
          type: str
          required: false
        native_vlan:
          description: Native VLAN
          type: str
          required: false
        tagged:
          description: tagged Native VLAN
          type: bool
          required: false
        admin_state:
          description: Administrative State
          type: str
          choices:
          - enabled
          - disabled
          required: false
        description:
          description: Port's description
          type: str
          required: false
        speed:
          description: Port's speed
          type: str
          required: false
        mtu:
          description: Port's MTU
          type: str
          required: false
        qsfp_mode:
          description: Port's split
          type: str
          required: false
        routed:
          description: Bridging or Routing mode
          type: bool
          required: false
        bpdu_filter:
          description: Enable BPDU Filtering
          type: str
          required: false
        bpdu_guard:
          description: Enable BPDU Guard
          type: str
          required: false
        root_guard:
          description: Enable Root Guard
          type: str
          required: false
        loop_guard:
          description: Enable Loop Guard
          type: str
          required: false
        tcn_guard:
          description: Enable TCN Guard
          type: str
          required: false
        admin_port_type:
          description: Enable STP Admin Port Type
          type: str
          choices:
          - admin-network
          - admin-edge
          required: false
        rpvst_guard:
          description: Enable RPVST Guard
          type: str
          required: false
        rpvst_filter:
          description: Enable RPVST Filtering
          type: str
          required: false
```

##### EXAMPLES

```YAML
-   name: Configure Ports using username and password
    arubanetworks.afc.afc_physical_interfaces:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            - switch: 10.10.10.7
              ports_config:
                - name: 1/1/37
                  native_vlan: 250
                - name: 1/1/38
                  native_vlan: 250
            - switch: 10.10.10.8
              ports_config:
                - name: 1/1/37
                  ungrouped_vlans: "250-252"
                  native_vlan: 250
                - name: 1/1/38
                  ungrouped_vlans: "250-252"
                  native_vlan: 250

-   name: Configure Ports using token
    arubanetworks.afc.afc_physical_interfaces:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            - switch: 10.10.10.7
              ports_config:
                - name: 1/1/37
                  native_vlan: 250
                - name: 1/1/38
                  native_vlan: 250
            - switch: 10.10.10.8
              ports_config:
                - name: 1/1/37
                  ungrouped_vlans: "250-252"
                  native_vlan: 250
                - name: 1/1/38
                  ungrouped_vlans: "250-252"
                  native_vlan: 250
```
