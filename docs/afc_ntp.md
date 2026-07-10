# module: afc_ntp

Description: This module creates or deletes a NTP configuration in the fabric.

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
  description: Operation to be performed on the NTP configuration, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Data of NTP configuration as depicted in the example. Required
    for create operation and not required for delete. Structure is provided in
    the example.
  type: dict
  suboptions:
    name:
      description: NTP Config name
      type: str
      required: true
    description:
      description: NTP Config description
      type: str
      required: false
    servers:
      description: NTP Servers to be used
      type: list
      elements: dict
      suboptions:
        server:
          description: NTP Server IP Address
          type: str
          required: true
        burst_mode:
          description: Type of the burst mode to use (if any).
          type: str
          choices:
          - burst
          - iburst
          required: false
        prefer:
          description: Preference flag to suggest for this association.
          type: bool
          default: true
          required: false
      required: true
    fabrics:
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
-   name: Create NTP configuration using username and password
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-NTP"
            fabrics:
                - "Test-Fabric"
            servers:
                -   server: "10.100.100.111"
                    burst_mode: "iburst"
                    prefer: True

-   name: Delete NTP configuration using username and password
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Test-NTP"

-   name: Create NTP configuration using token
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-NTP"
            servers:
                -   server: "10.100.100.111"
                    burst_mode: "iburst"
                    prefer: True

-   name: Delete NTP configuration using token
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        ntp_name: "Test-NTP"
        operation: "delete"
        data:
            name: "Test-NTP"
```
