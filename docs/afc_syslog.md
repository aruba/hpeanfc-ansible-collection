# module: afc_syslog

Description: This module creates or deletes a syslog configuration in the specified fabric.

##### ARGUMENTS

```YAML
afc_ip:
	description: >
		IP address of the Aruba Fabric Composer.
	type: str
	required: true
afc_username:
	description:
	- User account having permission to create VRF on the Aruba Fabric Composer
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
syslog_name:
	description: >
		Name of the Syslog Client Configuration to be created or deleted.
	type: str
	required: true
syslog_data:
	description: >
		Syslog client configuration data as per the example below.
	type: str
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
        syslog_name: "Test-Syslog"
        syslog_data:
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - 'Test-Fabric'

-   name: Delete syslog configuration using username and password
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        syslog_name: "Test-Syslog"
        operation: "delete"

-   name: Create syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        syslog_name: "Test-Syslog"
        syslog_data:
            entry_list:
            -   host: "10.14.121.35"
                port: 514
                severity: "ERROR"
                include_auditable_events: True
                transport: "tcp"
            facility: "LOCAL7"
            fabrics:
                - 'Test-Fabric'

-   name: Delete syslog configuration using token
    arubanetworks.afc.afc_syslog:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        syslog_name: "Test-Syslog"
        operation: "delete"
```
