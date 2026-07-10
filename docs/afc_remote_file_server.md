# module: afc_remote_file_server

Description: This module creates, updates or deletes a Remote File Transfer Server (RFTS) in HPE Aruba Networking Fabric Composer. A Remote File Transfer Server defines an SFTP/SCP endpoint used by AFC to transfer files such as backup archives.

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
  description: Operation to be performed on the Remote File Transfer Server, create,
    update or delete.
  type: str
  choices:
  - create
  - update
  - delete
  required: true
data:
  description: Data of the Remote File Transfer Server as depicted in the example.
    Required for create and update operations. For delete only the name is required.
  type: dict
  suboptions:
    name:
      description: Name of the Remote File Transfer Server.
      type: str
      required: true
    description:
      description: Description of the RFTS configuration.
      type: str
      required: false
    remote_file_server_hostname:
      description: Hostname or IP address of the remote host.
      type: str
      required: false
    protocol:
      description: File transfer protocol to be used.
      type: str
      choices:
      - sftp
      - scp
      required: false
    username:
      description: Username of the Remote File Transfer Server.
      type: str
      required: false
    password:
      description: Password of the Remote File Transfer Server for the above username.
      type: str
      required: false
    location:
      description: Base folder where the files need to be copied.
      type: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create a Remote File Transfer Server using username and password
    arubanetworks.afc.afc_remote_file_server:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: "Backup-Server"
            description: "SFTP backup target"
            remote_file_server_hostname: "10.100.100.50"
            protocol: "sftp"
            username: "backup"
            password: "backup_password"
            location: "/backups"

-   name: Update a Remote File Transfer Server
    arubanetworks.afc.afc_remote_file_server:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "update"
        data:
            name: "Backup-Server"
            remote_file_server_hostname: "10.100.100.51"

-   name: Delete a Remote File Transfer Server using token
    arubanetworks.afc.afc_remote_file_server:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "delete"
        data:
            name: "Backup-Server"
```
