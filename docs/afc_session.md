# module: afc_session

Description: This module creates or deletes a session to the HPE ANW Fabric Composer

##### ARGUMENTS

```YAML
afc_ip:
  description:
  - IP address of the HPE ANW Fabric Composer
  type: str
  required: true
afc_username:
  description:
  - User account having write permission on the HPE ANW Fabric Composer
  type: str
  required: true
afc_password:
  description:
  - Password of the user account
  type: str
  required: true
disable_tls_verification:
  description:
  - Disable TLS certificate verification when connecting to AFC.
  - Only enable this for AFC instances using self-signed certificates.
  type: bool
  required: false
  default: false
```

##### EXAMPLES

```YAML
-   name: Create a session and capture the auth_token
    arubanetworks.afc.afc_session:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        disable_tls_verification: true
    register: reg_afc_instance

-   name: Store the auth_token in a fact for re-use
    ansible.builtin.set_fact:
        auth_token: "{{ reg_afc_instance.auth_token }}"

-   name: Re-use the session with another module (token authentication)
    arubanetworks.afc.afc_fabric:
        afc_ip: "10.10.10.10"
        auth_token: "{{ auth_token }}"
        disable_tls_verification: true
        operation: create
        data:
            name: Aruba-Fabric
            timezone: Europe/London
```

##### NOTES

- When re-using an auth_token, do not also provide afc_username and afc_password. If they are provided, the session is closed because authentication is considered done via username and password only.
