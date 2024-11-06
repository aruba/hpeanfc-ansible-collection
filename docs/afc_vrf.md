# module: afc_vrf

Description: This module creates or deletes a VRF in the specified fabric.

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
		Name of the Fabric where the VRF will be created or deleted from.
	type: str
	required: true
operation:
	description: >
		Operation to be performed on the VRF, create or delete.
	type: str
	required: true
vrf_name:
	description: >
		Name of the VRF to be created or deleted.
	type: str
	required: true
vrf_data:
	description: >
		VRF specific data. Mandatory for create operation.
	type: dict
	required: false
```

##### EXAMPLES

```YAML
-   name: Create VRF using username and password
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "create"
        vrf_data:
            vni: 10000
            route_target:
                primary_route_target:
                    as_number: "65000:1"
                    address_family: "evpn"
                    evpn: False
                    route_mode: "both"
                    secondary_route_targets:
                        -   as_number: "1:1"
                            address_family: "evpn"
                            evpn: False
                            route_mode: "both"

-   name: Delete VRF using username and password
    arubanetworks.afc.afc_svi:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "delete"

-   name: Create VRF using token
    arubanetworks.afc.afc_vrf:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "create"
        vrf_data:
            vni: 10000
            route_target:
                primary_route_target:
                    as_number: "65000:1"
                    address_family: "evpn"
                    evpn: False
                    route_mode: "both"
                    secondary_route_targets:
                        -   as_number: "1:1"
                            address_family: "evpn"
                            evpn: False
                            route_mode: "both"

-   name: Delete VRF using token
    arubanetworks.afc.afc_svi:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        fabric_name: "Aruba-Fabric"
        vrf_name: "Aruba-VRF"
        operation: "delete"
```
