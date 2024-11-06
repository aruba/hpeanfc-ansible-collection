# Sample variables for the afc ansible collection

Description: This document contains the inputs that are needed for executing the modules via Ansible playbooks

##### Example variables and their structure

```YAML
---
# AFC Properties
afc_ip: "192.168.86.11"
afc_username: "admin"
afc_password: "password"

# Device list for discovery
devices_list:
  - '192.168.0.6'
  - '192.168.0.5'
  - '192.168.0.8'
  - '192.168.0.7'
  - '192.168.0.10'
  - '192.168.0.9'
  - '192.168.15'
  - '192.168.17'
  - '192.168.19'

# Device list for assignment
devices_assignment:
  '192.168.0.6': 'spine'
  '192.168.0.5': 'spine'
  '192.168.0.8': 'leaf'
  '192.168.0.7': 'leaf'
  '192.168.0.10': 'border_leaf'
  '192.168.0.9': 'border_leaf'

#devices_assignment:
#  '192.168.15': 'spine'
#  '192.168.17': 'leaf'
#  '192.168.19': 'border_leaf'

# Fabric properties
fabric_name: "Test-Fabric"
fabric_timezone: "Europe/London"

# Switch credentials
admin_passwd: "admin"
service_account_user: "afc_admin"
afc_admin_passwd: "admin-password"

# VRF Properties
vrf_name: 'VMWARE'
vrf_props:
  vni: 3001001
  route_target:
    primary_route_target:
      as_number: "65001:3001001"
      address_family: "evpn"
      evpn: false
      route_mode: "both"
      secondary_route_targets:
        - as_number: "1:3001001"
          address_family: "evpn"
          evpn: false
          route_mode: "both"

# BGP Properties
bgp_props:
  as_number: 65000
  name: "VMWARE"
  redistribute_ospf: false
  redistribute_connected: true
  redistribute_static: false
  redistribute_loopback: false
  enable: true
  trap_enable: false
  log_neighbor_changes: true
  fast_external_fallover: true
  maximum_paths: 8
  deterministic_med: true
  bestpath: true
  always_compare_med: true
  keepalive_timer: 60
  holddown_timer: 180

# L2VNI Properties
l2vni_props:
  fabric: "UK-VM02-FB01"
  devices:
    - "192.168.0.7"
    - "192.168.0.8"
    - "192.168.0.9"
    - "192.168.0.10"
  l2vni:
    system_mac_range: "Mac"
    as_number: '65000' ## Must be a string
    name_prefix: "Test-EVPN"
    rt_type: "ASN:VNI"
    vlans: '250' ## Must be a string
    vni_base: 10000
    description: "New L2VNI"
  ip_interface:
    vrf: "Test-VRF"
    enable: True
    local_proxy_arp_enabled: True
    name: "VLAN250"
    vlan: 250
    if_type: vlan
    ipv4_primary_address:
      address: 10.10.10.11-10.10.10.50
      prefix_length: 24
    active_gateway:
      ipv4_address: 10.10.10.1
      mac_address: 00:00:00:00:00:01
    switches:
      - "192.168.0.7"
      - "192.168.0.8"
      - "192.168.0.9"
      - "192.168.0.10"

# VLAN properties
vlan_id: 253

# VSX Properties
vsx:
  system_mac_range: Mac
  keepalive_ip_pool_range: IP
  name_prefix: VSX2
  keep_alive_interface_mode: routed
underlay:
  name: underlay
overlay:
  name: overlay

# VRF Properties
vrf_props_copy:
  name: "Test-Fabric"
  route_distinguisher: "loopback1:1"
  devices:
    - "192.168.0.7"
    - "192.168.0.8"
  bgp:
    same_config_than: "192.168.0.10"

# New Tenant Properties
tenant_props:
  fabric: "Test-Fabric"
  vrf:
    name: "Test-VRF"
    route_distinguisher: "loopback1:1"
    route_target:
      primary_route_target:
        as_number: '65000:1'
        evpn: False
        address_family: evpn
        route_mode: both
    vni: 30001
  bgp:
    as_number: 65000
    name: "Test-VRF"
    redistribute_ospf: True
    redistribute_connected: True
    redistribute_static: True
    redistribute_loopback: True
    enable: True
    trap_enable: True
    log_neighbor_changes: True
    fast_external_fallover: True
    maximum_paths: 8
    deterministic_med: True
    bestpath: True
    always_compare_med: True

# Ports configuration
ports_data:
  "192.168.0.10":
      "1/1/30":
        ungrouped_vlans: "250-252"
        native_vlan: 250
      "1/1/31":
        ungrouped_vlans: "250-252"
        native_vlan: 250
  "192.168.0.9":
      "1/1/30":
        ungrouped_vlans: "250-252"
        native_vlan: 250
      "1/1/31":
        ungrouped_vlans: "250-252"
        native_vlan: 250

# LAG Properties
lags:
  lag20:
    id: "20"
    ports:
      "192.168.0.10":
        - "1/1/33"
      "192.168.19":
        - "1/1/33"
    config:
      ungrouped_vlans: "250-260"
      native_vlan: "250"

# DSS Properties
dss_policy_name: "test_policy"
dss_policy_data:
  policy_subtype: "firewall"
  object_type: "policy"

dss_rule_name: 'test_rule'
dss_rule_data:
  action: "drop"
  source_endpoint_groups:
    - "test_eg"
  destination_endpoint_groups:
    - "test_eg"
  service_qualifiers:
    - "icmp"
    - "bgp"
    - "test_sq"

dss_eg_name: 'test_eg'
dss_eg_data:
  type: "layer3"
  endpoints:
    - vm_name: "UK-VM02-AFC01"
      vnic_name: "Network adapter 1"

dss_qualifier_name: "test_sq"
dss_qualifier_data:
  protocol_identifier:
    - src_port: "32"
      dst_port: "32"
      ip_protocol: "tcp"
  qualifier_type: "layer3"

# Syslog properties
syslog_name: 'Test-Syslog'
syslog_data:
  entry_list:
  - host: "10.14.121.35"
    port: 514
    severity: "ERROR"
    include_auditable_events: True
    transport: "tcp"
  facility: "LOCAL7"
  fabrics:
    - 'Test-Fabric'

# SNMP Properties
snmp_name: 'Test-SNMP'
snmp_data:
  fabrics: 'Test-Fabric'
  enable: True
  location: "eee"
  contact: "eee"
  community: "eee"
  agent_port: 161
  trap_port: 23
  users:
    - level: "auth"
      name: "eee"
      auth_type: "SHA"
      auth_pass: "eeeeeeeeee"
  servers:
    - address: "1.2.3.4"
      community: "eeeee"

# Radius properties
radius_name: 'Rest-Radius'
radius_data:
  config:
    secret: "test"
    server: "10.14.120.30"
    port: 1812

# DHCP Relay properties
dhcp_relay_name: 'Test-DHCP-Relay'
dhcp_relay_data:
  fabrics:
    - 'Test-Fabric'
  vlans: "251"
  ipv6_dhcp_mcast_server_addresses: []
  ipv6_dhcp_server_addresses: []
  ipv4_dhcp_server_addresses:
    - "1.2.3.4"

# DNS Properties
dns_name: 'Test-DNS'
dns_data:
  fabrics:
    - "Test-Fabric"
  domain_name: "hpe-france.eu"
  name_servers:
    - '10.14.120.211'

# STP Properties
stp_name: 'Test-STP'
stp_data:
  config_type: "mstp"
  configuration:
    mstp_config:
      config_revision: 0
      config_name: 'Test-STP-Config0'

# NTP Properties
ntp_name: 'Test-NTP'
ntp_data:
  fabrics:
    - "Test-Fabric"
  servers:
    - server: "10.14.120.211"
      burst_mode: "iburst"
      prefer: True

# VSX Properties
vsx_name: 'Test-VSX'
vsx_data:
  system_mac_range: 'Mac'
  keepalive_ip_pool_range: 'IP POOL'
  keep_alive_interface_mode: 'loopback'

# Underlay properties
underlay_name: 'Test-Underlay'
underlay_vrf: 'default'
underlay_data:
  ipv4_address: 'IP POOL'
  transit_vlan: 120

# Overlay properties
overlay_name: 'Test-Overlay'
overlay_vrf: 'default'
overlay_data:
  ipv4_address: 'IP POOL'
  spine_leaf_asn: "65100"

# PSM Integration properties (Not Tested)
psm_data:
  password: "PassworD"
  fabrics":
    - "Sense-DC1"
  host: "10.14.120.112"
  username: "admin"

# VMWare integration properties (Not Tested)
vmw_data:
  name: "vSphere"
  host: "10.14.120.51"
  username: "administrator@vsphere.local"
  password: "PassworD"
  description: ""
  enabled: True
  verify_ssl: False
  auto_discovery: True
  vlan_provisioning: True
  pvlan_provisioning: True
  downlink_vlan_range: "1-4094"
  vlan_range: "1-4094"
  pvlan_range: "1-4094"
  use_cdp: False
  downlink_vlan_provisioning: False
  storage_optimization: False
  endpoint_group_provisioning: True

# IPv4 Resource pool Data
resource_pool_data:
  type: 'IPv4'
  pool_ranges: "192.168.0.0/24"

# MAC Resource pool data
resource_pool_data:
    type: 'MAC'
    pool_ranges: "02:00:00:01:00:00-02:00:00:01:00:FF"

# Route map properties
route_map_name: 'Test-Route-Map'
route_map_data:
  switches: '192.168.0.11'
  entries:
    - seq: 10
      action: "deny"
      description: "ee"
      route_map_continue: 20
      match_vni: 10100
      set_origin: "igp"
    - seq: 20
      action: "deny"
      match_tag: 100

route_map_entry_name: 'Test-Route-Map-Entry'
route_map_entry_data:
  seq: 30
  action: "deny"
  set_local_preference: 1111
  match_interface: "1/1/1"

# Prefix list properties
prefix_list_name: 'Test-Prefix-List'
prefix_list_data:
  switches: '192.168.0.11'
  entries:
    - description: ""
      seq: 10
      action: "permit"
      prefix: "any"

prefix_list_entry_name: 'Test-Prefix-List-Entry'
prefix_list_entry_data:
  seq: 20
  action: "permit"
  prefix:
    address: "10.14.12.0"
    prefix_length: 24

# Community lists properties
community_list_name: 'Test-Community-List'
community_list_data:
  switches: '192.168.0.11'
  type: "community-expanded-list"
  entries:
    - description: ""
      seq: 10
      action: "deny"
      match_string: "internet"

# ASPath List properties
aspath_list_name: 'Test-AsPath-List'
aspath_list_data:
  switches: '192.168.0.11'
  entries:
    - description: ""
      seq: 10
      action: "deny"
      regex: "_65001$"

# OSPR Router properties
ospf_router_name: 'Test-OSPF-Router'
ospf_router_data:
  instance: "Test-OSPF-Router"
  switches: "192.168.0.11"
  id: 10
  redistribute:
    redistribute_bgp: false

# OSPR Area properties
ospf_area_name: 'Test-OSPF-Area'
ospf_area_data:
  ospf_router: "Test-OSPF-Router"
  switches: "192.168.0.11"
  area_id: 1

# OSPR Interface properties
ospf_int_name: 'Test-OSPF-Interface'
ospf_int_data:
  switch: "192.168.0.11"
  router: "10.10.10.254"
  area: "0.0.0.1"
  interface: "1/1/29"
  network_type: "ospf_iftype_pointopoint"

# Leaf spine properties
l3ls_data:
  name: 'Test-L3LS'
  pool_ranges: 'IP POOL'

# SFlow properties
sflow_name: 'Test-Sflow'
sflow_data:
  enable_sflow: False
  polling_interval: 20
  sampling_rate: 20000
  source_namespace: "management"
  collectors:
    - destination_port: 6343
      destination_ip_address: "192.168.56.12"
  fabrics: "Test-Fabric"
```
