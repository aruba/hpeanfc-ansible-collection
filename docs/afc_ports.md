# module: afc_ports

Description: This module is used to configure ports.

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
port_type:
  description: >
    Type of port configuration - Can be either physical por lag.
  type: str
  required: true
ports_data:
  description: >
    Port configuration data. Structure is provided in the example.
  type: dict
  required: true
```

##### EXAMPLES

```YAML
- name: Configure Ports using username and password
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    afc_username: "afc_admin"
    afc_password: "afc_password"
    port_type: "physical"
    ports_data:
      - switches: 10.10.10.7
        ports_config:
          - name: 1/1/37
            native_vlan: 250
          - name: 1/1/38
            native_vlan: 250
      - switches: 10.10.10.8
        ports_config:
          - name: 1/1/37
            ungrouped_vlans: "250-252"
            native_vlan: 250
          - name: 1/1/38
            ungrouped_vlans: "250-252"
            native_vlan: 250

- name: Configure LAG using username and password
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    afc_username: "afc_admin"
    afc_password: "afc_password"
    port_type: "lag"
    ports_data:
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

- name: Configure VSX LAG using username and password
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    afc_username: "afc_admin"
    afc_password: "afc_password"
    port_type: "lag"
    ports_data:
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

- name: Configure Ports using token
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
    port_type: "physical"
    ports_data:
      - switches: 10.10.10.7
        ports_config:
          - name: 1/1/37
            native_vlan: 250
          - name: 1/1/38
            native_vlan: 250
      - switches: 10.10.10.8
        ports_config:
          - name: 1/1/37
            ungrouped_vlans: "250-252"
            native_vlan: 250
          - name: 1/1/38
            ungrouped_vlans: "250-252"
            native_vlan: 250

- name: Configure LAG using token
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
    port_type: "lag"
    ports_data:
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

- name: Configure VSX LAG using token
  arubanetworks.afc.afc_ports:
    afc_ip: "10.10.10.10"
    auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
    port_type: "lag"
    ports_data:
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
