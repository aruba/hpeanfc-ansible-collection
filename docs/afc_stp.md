# module: afc_stp

Description: This module creates or deletes an STP configuration in the fabric.

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
  description: Operation to be performed on the STP configuration, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: STP configuration data. Structure is provided in the example.
  type: dict
  suboptions:
    name:
      description: STP Workflow Name
      type: str
      required: true
    fabrics:
      description: List of fabrics
      type: list
      elements: str
      required: false
    config_type:
      description: STP Type
      type: str
      choices:
      - mstp
      - rpvst
      default: mstp
      required: false
    configuration:
      description: SNMPv3 user
      type: list
      elements: dict
      suboptions:
        mstp_config:
          description: MSTP Configuration elements
          type: dict
          suboptions:
            config_revision:
              description: MSTP Configuration Revision
              type: int
              required: true
            config_name:
              description: MSTP Configuration Name
              type: int
              required: true
            instances:
              description: MSTP Instances configuration
              type: list
              elements: dict
              suboptions:
                instance_id:
                  description: MST region instance ID
                  type: str
                  required: true
                vlan_ids:
                  description: MST region VLAN IDs
                  type: str
                  required: true
        rpvst_config:
          description: RPVST Configuration elements
          type: dict
          suboptions:
            vlan_ids:
              description: RPVST Instance VLAN IDs
              type: str
              required: true
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Create STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-STP"
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using username and password
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "delete"
        data:
            name: "Test-STP"


-   name: Create STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-STP"
            config_type: "mstp"
            configuration:
                mstp_config:
                    config_revision: 0
                    config_name: 'Test-STP-Config0'

-   name: Delete STP configuration using token
    arubanetworks.afc.afc_stp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Test-STP"
```
