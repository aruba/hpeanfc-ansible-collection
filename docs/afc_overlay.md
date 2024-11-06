# module: afc_overlay

Description: This module creates or deletes an overlay configuration in the specified fabric.

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
		Name of the Fabric where an overlay configuration will be created or deleted from.
	type: str
	required: true
vrf_name:
	description: >
		Name of the VRF where overlay configuratoin needs to be applied.
	type: str
	required: true
overlay_name:
	description: >
		Name of the overlay.
	type: str
	required: true
overlay_data:
	description: >
		Overlay configuration data.
	type: dict
	required: true
```

##### EXAMPLES

```YAML
-   name: Create an overlay configuration using username and password
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        overlay_name: "Test-Overlay"
        overlay_data:
            ipv4_address: 'IP POOL'
            spine_leaf_asn: "65001"

-   name: Create an overlay configuration using token
    arubanetworks.afc.afc_overlay:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        overlay_name: "Test-Overlay"
        overlay_data:
            ipv4_address: 'IP POOL'
            spine_leaf_asn: "65001"
```
