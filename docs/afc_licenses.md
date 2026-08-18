# module: afc_licenses

Description: This module creates or deletes a licenses in AFC.

##### ARGUMENTS

```YAML
afc_ip:
  description: IP address of the HPE ANW Fabric Composer.
  type: str
  required: true
afc_username:
  description: User account having permission to push licenses on the HPE ANW
    Fabric Composer
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
  description: Operation to be performed on the license, create or delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: Data of licenses as depicted in the example.
  type: dict
  suboptions:
    license:
      description: License provided by Aruba. Required for 'create'
      type: str
      required: false
    license_key:
      description: License key found in AFC WebUI. Required for 'delete'
      type: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Push new license
    arubanetworks.afc.afc_licenses:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "server"
        operation: create
        data:
            license: {<license provided by HPE>}

-   name: Delete license
    arubanetworks.afc.afc_licenses:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "server"
        operation: delete
        data:
            license_key: ABCD12345DEF
```
