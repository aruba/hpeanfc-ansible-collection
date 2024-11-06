# module: afc_session

Description: This module creates an AFC session and also captures the Auth Key. This caputured auth_key can be used with rest of the modules to re-use existing session instead of creating new session for every action.

##### ARGUMENTS

```YAML
afc_ip:
    description:
    - IP address of the Aruba Fabric Composer
    type: str
    required: true
afc_username:
    description:
    - User account having permission to create VRF on the Aruba Fabric Composer
    type: str
    required: true
afc_password:
    description:
    - Password of the user account
    type: str
    required: true
```

##### EXAMPLES

```YAML
-   name: Create Session
    arubanetworks.afc.afc_session:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
    register: reg_afc_instance

-   name: Capture the auth_token
    ansible.builtin.set_fact:
        auth_token: "{{ reg_afc_instance['auth_token'] }}
```
