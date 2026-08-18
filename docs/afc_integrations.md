# module: afc_integrations

Description: This module configures integrations with supported 3rd Party solutions.

##### ARGUMENTS

```YAML
afc_ip:
  description:
  - IP address of the HPE ANW Fabric Composer.
  type: str
  required: true
afc_username:
  description:
  - User account having write permission on the HPE ANW Fabric Composer.
  type: str
  required: false
afc_password:
  description:
  - Password of the user account.
  type: str
  required: false
auth_token:
  description:
  - Auth token from the create session playbook.
  type: str
  required: false
disable_tls_verification:
  description:
  - Disable TLS certificate verification when connecting to AFC.
  - Only enable this for AFC instances using self-signed certificates.
  type: bool
  required: false
  default: false
operation:
  description:
  - Operation to be performed on the integration configuration.
  - create or delete.
  type: str
  choices:
  - create
  required: true
data:
  description:
  - Integration configuration data. Structure is provided in the example.
  type: dict
  required: true
  suboptions:
    type:
      description:
      - Type of integration.
      type: str
      choices:
      - vm_vsphere
      - pensando_psm
      required: true
    host:
      description:
      - Integration's IP Address.
      type: str
      required: true
    username:
      description:
      - Integration's Username.
      type: str
      required: true
    password:
      description:
      - Integration's Password.
      type: str
      required: true
    enabled:
      description:
      - Integration's Status.
      type: bool
      default: true
      required: false
    verify_ssl:
      description:
      - SSL verification.
      type: bool
      default: false
      required: false
    auto_discovery:
      description:
      - VMware specific. Auto-Discovery of hosts.
      type: bool
      default: true
      required: false
    vlan_provisioning:
      description:
      - VMware specific. Indicates whether VLANs will be automatically provisioned.
      type: bool
      default: false
      required: false
    downlink_vlan_provisioning:
      description:
      - VMware specific. Indicates whether VLANs will be automatically provisioned
        for downlink switches.
      type: bool
      default: false
      required: false
    pvlan_provisioning:
      description:
      - VMware specific. Indicates whether Private VLANs will be automatically
        provisioned.
      type: bool
      default: false
      required: false
    downlink_vlan_range:
      description:
      - VMware specific. No actions will be taken on VLANs outside this range.
      type: str
      required: false
    vlan_range:
      description:
      - VMware specific. No actions will be taken on VLANs outside this range.
      type: str
      required: false
    pvlan_range:
      description:
      - VMware specific. No actions will be taken on VLANs outside this range.
      type: str
      required: false
    use_cdp:
      description:
      - VMware specific. Indicates whether CDP should be used instead of LLDP
        as the Discovery Protocol for Distributed vSwitches.
      type: bool
      default: false
      required: false
    storage_optimization:
      description:
      - VMware specific. Indicates if vSAN network traffic will be optimized through
        the use of policies.
      type: bool
      default: false
      required: false
    endpoint_group_provisioning:
      description:
      - VMware specific. Indicates whether auto creation of Endpoint group based
        on VM tags is enabled.
      type: bool
      default: false
      required: false
    cumulative_epg_provisioning:
      description:
      - VMware specific. Indicates whether auto creation of Cumulative endpoint
        group based on VM tags is enabled.
      type: bool
      default: false
      required: false
```

##### EXAMPLES

```YAML
-   name: Configure a VMware vSphere integration using username and password
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        afc_username: "admin"
        afc_password: "password"
        operation: create
        data:
            type: vm_vsphere
            host: "10.20.30.40"
            username: "administrator@vsphere.local"
            password: "vsphere_password"
            enabled: true
            auto_discovery: true
            vlan_provisioning: true
            vlan_range: "100-200"

-   name: Configure a Pensando PSM integration using an existing session
    arubanetworks.afc.afc_integrations:
        afc_ip: "10.10.10.10"
        auth_token: "{{ auth_token }}"
        disable_tls_verification: true
        operation: create
        data:
            type: pensando_psm
            host: "10.20.30.50"
            username: "admin"
            password: "psm_password"
            enabled: true
```
