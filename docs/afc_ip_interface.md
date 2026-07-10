# module: afc_ip_interface

Description: This module is used to create and delete SVI, a Loopback or a Routed Port.

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
  description: Operation to be performed with the IP Interface, ROP, loopback
    or SVI, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: IP Interface data containing if_type, vlan, active_gateway, ipv4_primary_address,
    local_proxy_arp_enabled and the switches. The values vlan and the prefix_length
    need to be integers. Structure is provided in the example.
  type: dict
  suboptions:
    fabric:
      description: Fabric Name
      type: str
      required: true
    vrf:
      description: VRF Name
      type: str
      required: true
    name:
      description: IP Interface Name
      type: str
      required: true
    enable:
      description: IP Interface's Status.
      type: bool
      default: true
      required: false
    local_proxy_arp_enabled:
      description: Enable or disable local proxy arp.
      type: bool
      default: false
      required: false
    vlan:
      description: VLAN to be mapped to the IP Interface.
      type: int
      required: false
    if_type:
      description: IP Interface type.
      type: str
      choices:
      - vlan
      - routed
      - loopback
      required: true
    ipv4_primary_address:
      description: Primary IPv4 to be configured.
      type: dict
      required: true
      suboptions:
        address:
          description: IPv4 Address. Can IPv4 Address or Range
          type: str
          required: true
        prefix_length:
          description: IPv4 Prefix length.
          type: int
          required: true
    active_gateway:
      description: Active Gateway to be configured.
      type: dict
      required: false
      ipv4_address:
        description: IPv4 Address.
        type: str
        required: true
      mac_address:
        description: MAC Address.
        type: str
        required: true
    switches:
      description: List of Switches
      type: list
      elements: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create IP Interface using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "VLAN250"
            vlan: 250
            if_type: vlan
            ipv4_primary_address:
                address: "10.10.10.11-10.10.10.50"
                prefix_length: 24
            active_gateway:
                ipv4_address: "10.10.10.1"
                mac_address: "00:00:00:00:00:01"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Create a ROP (Routed Only Port) using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "ROP to External Router"
            interface: 1/1/14
            if_type: routed
            ipv4_primary_address:
                address: "10.10.10.25"
                prefix_length: 24
            switches:
                - "10.10.10.7"

-   name: Create an SVI using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "VLAN250"
            vlan: 250
            if_type: vlan
            ipv4_primary_address:
                address: "10.10.10.11-10.10.10.50"
                prefix_length: 24
            active_gateway:
                ipv4_address: "10.10.10.1"
                mac_address: "00:00:00:00:00:01"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Create a loopback interface using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            if_type: loopback
            name: loopback10
            ipv4_primary_address:
                address: "10.10.10.32"
                prefix_length: 32
            switches:
                - "10.10.10.7"

-   name: Delete IP Interface using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "VLAN250"
            switches:
                - "10.10.10.7"

-   name: Delete a ROP (Routed Only Port) using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: 1/1/14
            switches:
                - "10.10.10.7"

-   name: Delete an SVI using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "VLAN250"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Delete a loopback interface using username and password
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: loopback10
            switches:
                - "10.10.10.7"

-   name: Create IP Interface using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "VLAN250"
            vlan: 250
            if_type: vlan
            ipv4_primary_address:
                address: "10.10.10.11-10.10.10.50"
                prefix_length: 24
            active_gateway:
                ipv4_address: "10.10.10.1"
                mac_address: "00:00:00:00:00:01"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Create a ROP (Routed Only Port) using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "ROP to External Router"
            interface: 1/1/14
            if_type: routed
            ipv4_primary_address:
                address: "10.10.10.25"
                prefix_length: 24
            switches:
                - "10.10.10.7"

-   name: Create an SVI using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            local_proxy_arp_enabled: True
            name: "VLAN250"
            vlan: 250
            if_type: vlan
            ipv4_primary_address:
                address: "10.10.10.11-10.10.10.50"
                prefix_length: 24
            active_gateway:
                ipv4_address: "10.10.10.1"
                mac_address: "00:00:00:00:00:01"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Create a loopback interface using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            enable: True
            if_type: loopback
            name: loopback10
            ipv4_primary_address:
                address: "10.10.10.32"
                prefix_length: 32
            switches:
                - "10.10.10.7"

-   name: Delete IP Interface using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "VLAN250"
            switches:
                - "10.10.10.7"

-   name: Delete a ROP (Routed Only Port) using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "ROP1"
            switches:
                - "10.10.10.7"

-   name: Delete an SVI using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: "VLAN250"
            switches:
                - "10.10.10.7"
                - "10.10.10.8"
                - "10.10.10.9"

-   name: Delete a loopback interface using token
    arubanetworks.afc.afc_ip_interface:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            fabric: "Aruba-Fabric"
            vrf: "Aruba-VRF"
            name: loopback10
            switches:
                - "10.10.10.7"
```
