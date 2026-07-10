# module: afc_sflow

Description: This module creates or deletes a SFlow configuration.

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
disable_tls_verification:
  description: Disable TLS certificate verification when connecting to AFC. Only
    enable this for AFC instances using self-signed certificates.
  type: bool
  required: false
  default: false
operation:
  description: Operation to be performed on the SFlow configuration, create or
    delete.
  type: str
  choices:
  - create
  - delete
  required: true
data:
  description: SFlow configuration as per the example below.
  type: dict
  suboptions:
    name:
      description: sFlow Config name
      type: str
      required: true
    description:
      description: sFlow Config description
      type: str
      required: false
    polling_interval:
      description: Polling Interval.
      type: int
      default: 20
      required: false
    sampling_rate:
      description: Sampling Rate.
      type: int
      default: 20000
      required: false
    source_namespace:
      description: VRF to export flows.
      type: str
      default: management
      required: false
    source_ip_address:
      description: Source IP address.
      type: str
      required: false
    collectors:
      description: External Collectors information
      type: list
      elements: dict
      suboptions:
        destination_ip_address:
          description: Destination IP address.
          type: str
          required: true
        destination_port:
          description: Destination UDP port.
          type: str
          required: false
      required: true
    fabrics:
      description: List of Fabrics
      type: list
      elements: str
      required: false
    switches:
      description: List of Switches
      type: list
      elements: str
      required: false
  required: true
```

##### EXAMPLES

```YAML
-   name: Create a SFlow configuration using username and password
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        operation: "create"
        data:
            name: Test-Sflow
            enable_sflow: true
            polling_interval: 20
            sampling_rate: 20000
            collectors:
                -   destination_port: 6343
                    destination_ip_address: "192.168.56.12"
            fabrics: "Test-Fabric"

-   name: Delete a SFlow configuration using username and password
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
        data:
            name: "Test-Sflow"
        operation: "delete"

-   name: Create a SFlow configuration using token
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        operation: "create"
        operation: "create"
        data:
            name: Test-Sflow
            enable_sflow: false
            polling_interval: 20
            sampling_rate: 20000
            source_namespace: "management"
            collectors:
                -   destination_port: 6343
                    destination_ip_address: "192.168.56.12"
            fabrics: "Test-Fabric"

-   name: Delete a SFlow configuration using token
    arubanetworks.afc.afc_sflow:
        afc_ip: "10.10.10.10"
        auth_token: "xxlkjlsdfluwoeirkjlkjsldjjjlkj23423ljlkj"
        data:
            name: "Test-Sflow"
        operation: "delete"
```
