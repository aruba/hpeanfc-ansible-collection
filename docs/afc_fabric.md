# module: afc_fabric

Description: This module is used to create, delete a fabric or assign multiple switches to the specified fabric along with role.

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
fabric_name:
	description: >
		Name of the Fabric.
	type: str
	required: true
operation:
	description: >
			Operation to be performed with the Fabric, create or delete or assign
	type: str
	required: true
fabric_timezone:
	description: >
		Fabric timezone, needed for create operation
	type: str
	required: false
devices_assignment:
	description: >
		Device assignment. The dictionary to contain IP addresses as key and roles as the value.
	type: dict
	required: true
```

##### EXAMPLES

```YAML
-   name: Create Fabric using usename and password
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        fabric_timezone: "Europe/London"
        operation: "create"

-   name: Delete Fabric using usename and password
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "delete"
-   name: Assign multiple switches to the Fabric and assign role using usename and password
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        operation: "assign"
        devices_assignment:
            10.10.10.11: "leaf"
            10.10.10.12: "leaf"

-   name: Create Fabric using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        fabric_timezone: "Europe/London"
        operation: "create"

-   name: Delete Fabric using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "delete"
-   name: Assign multiple switches to the Fabric and assign role using token
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        operation: "assign"
        devices_assignment:
            10.10.10.11: "leaf"
            10.10.10.12: "leaf"
```
