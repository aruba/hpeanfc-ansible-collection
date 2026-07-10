# module: afc_ports

Description: This module is used to configure ports.

##### ARGUMENTS

```YAML
afc_ip:
  description: IP address of the Aruba Fabric Composer.
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
  description: Auth token from the create session playbook.
  type: str
  required: false
disable_tls_verification:
  description: Disable TLS certificate verification when connecting to AFC. Only
    enable this for AFC instances using self-signed certificates.
  type: bool
  required: false
  default: false
fabric_name:
  description: Name of the Fabric.
  type: str
  required: true
ports_data:
  description: Port configuration data.
  type: dict
  required: true
```

##### EXAMPLES

```YAML
-   name: Configure Ports
    arubanetworks.afc.afc_ports:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        ports_data:
            10.10.10.7:
                "1/1/30":
                    native_vlan: 250
                "1/1/31":
                    native_vlan: 250
            10.10.10.8:
                "1/1/30":
                    native_vlan: 250
                "1/1/31":
                    native_vlan: 250
```
