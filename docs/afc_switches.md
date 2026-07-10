# module: afc_switches

Description: This module allows to manage switches on and through HPE ANW Fabric Composer.

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
  description: 'Operation to be performed on the switch - One of : update, reconcile,
    reboot, save.'
  type: str
  choices:
  - update
  - save
  - reconcile
  - reboot
  required: true
data:
  description: Data used to act on switches. Structre is provided in the example.
  type: dict
  suboptions:
    boot_partition:
      description: Reboot specific. Partition which will be used by device to
        reboot.
      type: list
      choices:
      - primary
      - secondary
      - active
      - non-active
      default: active
      required: false
    fabric:
      description: List of Fabrics
      type: list
      elements: str
      required: false
    switches:
      description: List of Switches
      type: list
      elements: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Update switch data on AFC using username and password
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "update"
        data:
            switches: "10.10.10.15"
            name: "Updated_Switch_Name"

-   name: Reconcile switch on AFC using username and password
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reconcile"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"

-   name: Reboot a set of switches through AFC using username and password
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reboot"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            boot_partition: 'active'

-   name: Reboot all switches in Fabric through AFC using username and password
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reboot"
        data:
            fabric:
                - "DC-Fabric"
            boot_partition: 'non-active'

-   name: Reboot all switches in DC-Fabric and a set of devices using username
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "reboot"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"
            boot_partition: 'non-active'

-   name: Save configuraton on switches through AFC using username and password
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "save"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"

-   name: Update switch data on AFC using token
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "update"
        data:
            switches: "10.10.10.15"
            name: "Update_Switch_Name"

-   name: Reconcile switch on AFC using token
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reconcile"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"

-   name: Reboot switch through AFC using token
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "reboot"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"
            boot_partition: 'non-active'

-   name: Save configuraton on switches through AFC using token
    arubanetworks.afc.afc_switches:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "save"
        data:
            switches:
                - "10.10.10.15"
                - "10.10.10.16"
            fabric:
                - "DC-Fabric"
```
