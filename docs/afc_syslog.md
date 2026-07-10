# module: afc_syslog

Description: This module creates or deletes a syslog client configuration.

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
  description: Operation to be performed on the Syslog configuration, create or
    delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Syslog client configuration data as per the example below.
  type: str
  suboptions:
    name:
      description: DHCP Relay Config name
      type: str
      required: true
    description:
      description: DHCP Relay Config description
      type: str
      required: false
    facility:
      description: Facility level. Set to USER when syslog is created only for
        HPE ANW Fabric Composer
      type: str
      choices:
      - LOCAL0
      - LOCAL1
      - LOCAL2
      - LOCAL3
      - LOCAL4
      - LOCAL5
      - LOCAL6
      - LOCAL7
      - USER
      required: false
    logging_persistent_storage:
      description: Enables Persistent Storage
      type: dict
      suboptions:
        severity:
          description: Log Severity.
          type: str
          choices:
          - EMERG
          - ALERT
          - CRIT
          - ERROR
          - WARNING
          - NOTICE
          - INFO
          - DEBUG
          default: INFO
          required: false
        enable:
          description: Enable Persistent Storage.
          type: bool
          default: true
          required: false
      required: false
    entry_list:
      description: Enables Persistent Storage
      type: list
      elements: dict
      suboptions:
        host:
          description: Syslog Server IPv4/v6 Address or hostname.
          type: str
          required: true
        port:
          description: Syslog Server Port.
          type: int
          required: false
        severity:
          description: Log Severity.
          type: str
          choices:
          - EMERG
          - ALERT
          - CRIT
          - ERROR
          - WARNING
          - NOTICE
          - INFO
          - DEBUG
          default: INFO
          required: false
        include_auditable_events:
          description: Specifies whether auditable events should be transmitted
            to the remote syslog server
          type: bool
          default: true
          required: false
        unsecure_tls_renegotiation:
          description: Enable TLS session with syslog server which does not support
            secure renegotiation.
          type: bool
          default: true
          required: false
        tls_auth_mode:
          description: TLS authentication mode used to authenticate the server
          type: str
          choices:
          - certificate
          - subject-name
          required: false
        transport:
          description: Transport layer protocol used to forward messages to the
            server.
          type: str
          choices:
          - udp
          - tcp
          - tls
          default: udp
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
-   name: Create syslog configuration using username and password
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Test-Syslog"
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - "Test-Fabric"

-   name: Delete syslog configuration using username and password
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Syslog"
        operation: "delete"

-   name: Create syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        data:
            name: "Test-Syslog"
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - "Test-Fabric"

-   name: Delete syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Syslog"
        operation: "delete"
```
