# module: afc_lag_interfaces

Description: This module is used to configure LAG Interfaces.

##### ARGUMENTS

```YAML
afc_ip:
  description: IP address of the HPE ANW Fabric Composer.
  type: str
  required: true
afc_username:
  description: User account having write permission on the HPE ANW Fabric Composer
  type: str
  required: false
afc_password:
  description: Password of the user account
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
  type: dict
  suboptions:
    lag_name:
      description: LAG Name
      type: str
      required: true
    lag_id:
      description: LAG ID
      type: int
      required: true
    ports:
      description: Physical ports to ne mapped to the LAG
      type: list
      elements: dict
      suboptions:
        switch:
          description: Switch IP Address
          type: str
          required: true
        ports:
          description: List of physical ports on that switch
          type: list
          elements: str
          required: true
    global_config:
      description: Global LAG configuration
      type: dict
      suboptions:
        ungrouped_vlans:
          description: set of VLANs to be configured
          type: str
          required: true
        native_vlan:
          description: Native VLAN
          type: list
          required: true
        tagged:
          description: tagged Native VLAN
          type: bool
          required: true
        lacp_fallback:
          description: LACP Fallback Enabled
          type: bool
          required: true
        enable_lossless:
          description: Lossless enabled
          type: bool
          required: true
    lacp_config:
      description: LACP-related configuration
      type: dict
      suboptions:
        interval:
          description: LACP Rate
          type: str
          choices:
          - slow
          - fast
          required: true
    speed_config:
      description: Speed-related configuration
      type: dict
      suboptions:
        speed:
          description: LAG's speed Rate
          type: str
          required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Configure LAG using username and password
    arubanetworks.afc.afc_lag_interfaces:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            lag_name: 'lag15'
            lag_id: 15
            ports:
                - switch: "10.10.10.7"
                  ports:
                    - "1/1/10"
                    - "1/1/11"
            global_config:
                ungrouped_vlans: "1253-1254"
                native_vlan: 1
                lacp_fallback: False
            lacp_config:
                interval: "fast"

-   name: Configure VSX LAG using username and password
    arubanetworks.afc.afc_lag_interfaces:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            lag_name: 'lag15'
            lag_id: 15
            ports:
                - switch: "10.10.10.7"
                  ports:
                    - "1/1/10"
                - switch: "10.10.10.8"
                  ports:
                    - "1/1/10"
            global_config:
                ungrouped_vlans: "1253-1254"
                native_vlan: 1
                lacp_fallback: False
            lacp_config:
                interval: "fast"

-   name: Configure LAG using token
    arubanetworks.afc.afc_lag_interfaces:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            lag_name: 'lag15'
            lag_id: 15
            ports:
                - switch: "10.10.10.7"
                  ports:
                    - "1/1/10"
                    - "1/1/11"
            global_config:
                ungrouped_vlans: "1253-1254"
                native_vlan: 1
                lacp_fallback: False
            lacp_config:
                interval: "fast"

-   name: Configure VSX LAG using token
    arubanetworks.afc.afc_lag_interfaces:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            lag_name: 'lag15'
            lag_id: 15
            ports:
                - switch: "10.10.10.7"
                  ports:
                    - "1/1/10"
                - switch: "10.10.10.8"
                  ports:
                    - "1/1/10"
            global_config:
                ungrouped_vlans: "1253-1254"
                native_vlan: 1
                lacp_fallback: False
            lacp_config:
                interval: "fast"
```
