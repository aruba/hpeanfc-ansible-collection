# module: afc_vlan

Description: This Ansible module facilitates the creation or deletion of VLANs in a fabric managed by the HPE ANW Fabric Composer. It creates VLANs based on specified names and IDs and updates their configuration within the fabric.

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
  description: Operation to be performed with the VLAN, create, update or delete
  type: str
  choices:
  - create
  - update
  - delete
  required: true
data:
  description: Data to manipulate VLANs.
  type: dict
  suboptions:
    type:
      description: VLAN type.
      type: str
      choices:
      - vlan
      - vlan_group
      - stretched_vlan
      required: true
    name:
      description: VLAN Name.
      type: str
      required: true
    description:
      description: VLAN Description.
      type: str
      required: false
    fabric:
      description: VLAN specific. Name of the Fabric on which the VLAN(s) are
        managed.
      type: str
      required: false
    vlan_id:
      description: VLAN specific. VLAN range(s), e.g. "10" or "10,20-30".
      type: str
      required: false
    vlan_name:
      description: VLAN specific. Name given to the VLAN(s). Renaming an existing
        VLAN is dependent on the AFC version and may be a no-op on some releases;
        assigning devices always applies.
      type: str
      required: false
    switches:
      description: VLAN specific. List of devices (IP address or name) to which
        the VLAN(s) are assigned or from which they are unassigned.
      type: list
      elements: str
      required: false
    fabric_scope:
      description: VLAN specific. Alternative to switches to scope the VLAN creation.
      type: str
      choices:
      - include_spine
      - exclude_spine
      required: false
    strict_firewall_bypass_enabled:
      description: VLAN specific. Enable strict firewall bypass on the VLAN(s).
      type: bool
      required: false
    vlans:
      description: VLAN Group specific. VLANs list.
      type: str
      required: false
    fabrics:
      description: Stretched VLAN Specific. List of Fabrics
      type: list
      elements: str
      required: false
    stretched_vlans:
      description: Stretched VLAN Specific. Stretched VLAN ID.
      type: str
      required: false
    global_route_targets:
      description: Stretched VLAN Specific. Global Route Targets.
      type: list
      required: false
      elements: dict
      suboptions:
        rt_type:
          description: Route Target Type.
          type: str
          choices:
          - NN:VLAN
          - NN:VNI
          required: false
        administrative_number:
          description: AS Number to be used.
          type: str
          required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create VLANs and assign them to devices using username and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: create
        data:
            type: vlan
            fabric: DC1
            vlan_id: "100,200-202"
            vlan_name: Production
            switches:
                - 10.149.2.10
                - Leaf-1

-   name: Assign an existing VLAN to additional devices and rename it
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: update
        data:
            type: vlan
            fabric: DC1
            vlan_id: "100"
            vlan_name: Prod-Renamed
            switches:
                - Leaf-2

-   name: Unassign a VLAN from specific devices
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: delete
        data:
            type: vlan
            fabric: DC1
            vlan_id: "100"
            switches:
                - Leaf-2

-   name: Delete VLANs from the whole Fabric
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: delete
        data:
            type: vlan
            fabric: DC1
            vlan_id: "100,200-202"

-   name: Create a VLAN Group in HPE ANW Fabric Composer using username
          and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: create
        data:
            type: vlan_group
            name: Test-VLANGroup
            description: New VLAN Group
            vlans: "23,56-58"

-   name: Delete a VLAN Group in HPE ANW Fabric Composer using username
          and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: "delete"
        data:
            name: Test-VLANGroup
            name: Test

-   name: Create a VLAN Group in HPE ANW Fabric Composer using token
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: create
        data:
            type: vlan_group
            name: Test-VLANGroup
            description: New VLAN Group
            vlans: "23,56-58"

-   name: Delete a VLAN Group in HPE ANW Fabric Composer using token
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: Test-VLANGroup
            name: Test

-   name: Create a Stretched VLAN in HPE ANW Fabric Composer using username
          and password
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: create
        data:
            type: stretched_vlan
            fabrics:
                - DC1
                - DC2
            stretched_vlans: 301
            global_route_targets:
                - rt_type: NN:VLAN
                  administrative_number: 1

-   name: Create a VLAN Group in HPE ANW Fabric Composer using token
    arubanetworks.afc.afc_vlan:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: create
        data:
            type: stretched_vlan
            fabrics:
                - DC1
                - DC2
            stretched_vlans: 301
            global_route_targets:
                - rt_type: NN:VLAN
                  administrative_number: 1
```
