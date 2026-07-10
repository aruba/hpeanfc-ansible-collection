# module: afc_cli

Description: This module sends CLI commands onto devices through HPEANFC and sends back the outputs.

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
  description: Data to be used to send commands. Each command will be executed
    on every switch provided. Register the output to a variable or execute the
    playbook in verbose mode to observe the results of the commands.
  type: dict
  suboptions:
    switches:
      description: List of switches to send commands to
      type: list
      elements: str
      required: true
    commands:
      description: List of commands to send to switches
      type: list
      elements: str
      required: true
  required: true
```

##### EXAMPLES

```YAML
-   name: Run list of commands on switches using username and password
    arubanetworks.afc.afc_cli:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            switches:
                - "10.10.10.14"
                - "10.10.10.15"
            commands:
                - "show arp"
                - "show bgp all summary"

-   name: Run list of commands on switches using the token
    arubanetworks.afc.afc_cli:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            switches:
                - "10.10.10.14"
                - "10.10.10.15"
            commands:
                - "show arp"
                - "show bgp all summary"
```
