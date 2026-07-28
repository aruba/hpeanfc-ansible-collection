# module: afc_vsx

Description: This module creates or deletes a VSX configuration in the specified fabric.

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
  description: Operation to be performed on the VSX, create or reapply, delete
    not supported.
  type: str
  choices:
  - create
  - reapply
  - delete
  required: true
data:
  description: VSX configuration data as specified in the example below.
  type: dict
  suboptions:
    name:
      description: VSX Config name
      type: str
      required: true
    fabric:
      description: Fabric on which the VSX worflow will be applied
      type: str
      required: true
    system_mac_range:
      description: MAC Resource Pool used for VSX System Mac
      type: str
      required: true
    keepalive_ip_pool_range:
      description: IPv4 Resource Pool used for KeepAlive. Not required when
        keep_alive_interface_mode is management_interface.
      type: str
      required: false
    keep_alive_interface_mode:
      description: IP interface mode used for Keep alive interface. The
        management_interface mode (keep alive over the management VRF) is only
        available from AFC version 7.3 onwards.
      type: str
      choices:
      - routed
      - loopback
      - management_interface
      required: true
    keep_alive_vrf:
      description: Name of the VRF used for the keep alive interface (for example
        mgmt). Using the management (mgmt) VRF is only available from AFC version
        7.3 onwards.
      type: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"
            system_mac_range: "MAC POOL"
            keepalive_ip_pool_range: "IP POOL"
            keep_alive_interface_mode: "loopback"

-   name: Create VSX over the management (mgmt) VRF (AFC 7.3+)
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"
            system_mac_range: "MAC POOL"
            keep_alive_interface_mode: "management_interface"
            keep_alive_vrf: "mgmt"

-   name: Reapply VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reapply"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"

-   name: Delete VSX using username and password
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"

-   name: Create VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"
            system_mac_range: "MAC POOL"
            keepalive_ip_pool_range: "IP POOL"
            keep_alive_interface_mode: "loopback"

-   name: Reapply VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reapply"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"

-   name: Delete VSX using token
    arubanetworks.afc.afc_vsx:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Test-VSX"
            fabric: "Aruba-Fabric"
```
