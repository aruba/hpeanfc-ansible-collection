# module: afc_ntp

Description: This module creates or deletes a NTP configuration in the specified fabric.

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
operation:
	description: >
		Operation to be performed on the NTP configuration, create or delete.
	type: str
	required: true
ntp_name:
	description: >
		Name of the NTP Entry.
	type: str
	required: true
ntp_data:
	description: >
		Data of NTP configuration as depicted in the example. Required for create operation and not required for delete.
	type: dict
	required: false
```

##### EXAMPLES

```YAML
-   name: Create NTP configuration using username and password
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        ntp_name: "Test-NTP"
        operation: "create"
        ntp_data:
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
        ntp_name: "Test-NTP"
        operation: "delete"

-   name: Create NTP configuration using token
    arubanetworks.afc.afc_ntp:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        ntp_name: "Test-NTP"
        operation: "create"
        ntp_data:
            fabrics:
                - "Test-Fabric"
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
```
