# module: afc_evpn_settings

Description: This module updates the global (fabric-wide) EVPN settings such as ARP suppression, local SVI, local MAC and the VXLAN tunnel bridging mode.

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
  description: Operation to be performed on the EVPN settings.
  type: str
  choices:
  - update
  required: true
data:
  description: Global EVPN settings data.
  type: dict
  suboptions:
    fabric:
      description: Fabric Name.
      type: str
      required: true
    arp_suppression:
      description: Enable or disable ARP suppression.
      type: bool
      required: true
    local_svi:
      description: Enable or disable local SVI.
      type: bool
      required: false
    local_mac:
      description: Enable or disable local MAC.
      type: bool
      required: false
    vxlan_tunnel_bridging_mode:
      description: VXLAN tunnel bridging mode.
      type: str
      choices:
      - ibgp-ebgp
      - no-bridging
      required: false
    switches:
      description: List of switches on which to apply the settings. If not
        specified, the settings apply to the whole fabric.
      type: list
      elements: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Update EVPN settings using username and password
    arubanetworks.afc.afc_evpn_settings:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "update"
        data:
            fabric: "Aruba-Fabric"
            arp_suppression: true
            local_svi: true
            local_mac: true
            vxlan_tunnel_bridging_mode: "ibgp-ebgp"

-   name: Update EVPN settings using token
    arubanetworks.afc.afc_evpn_settings:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "update"
        data:
            fabric: "Aruba-Fabric"
            arp_suppression: true
```
