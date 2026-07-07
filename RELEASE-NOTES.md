# Unreleased

### ⚠️ Breaking Changes

#### TLS certificate verification is now enabled by default
The collection relies on `pyafc`, which previously connected to AFC with TLS
certificate verification **disabled**. Verification is now enabled by
default, and every module exposes a new `disable_tls_verification` option.

- **Who is affected:** any playbook targeting an AFC that presents a
  self-signed or otherwise untrusted certificate (common in labs and on
  appliances using the factory certificate).
- **Symptom after upgrade:** the task fails with a TLS certificate
  verification error instead of connecting.
- **How to keep the previous behaviour:** set `disable_tls_verification: true`
  on the module (or on `afc_session`). Only do this for trusted/lab
  environments.

  ```yaml
  - name: Configure a VRF on a lab AFC using a self-signed certificate
    arubanetworks.afc.afc_vrf:
      afc_ip: "10.10.10.10"
      afc_username: "admin"
      afc_password: "password"
      disable_tls_verification: true   # self-signed / lab certificate only
      operation: create
      data: "{{ vrf_data }}"
  ```

  The recommended long-term fix is to install a trusted certificate on AFC so
  that verification can stay enabled (the default).

### Security Fixes
- Marked `afc_password` and `auth_token` as `no_log` in every module so the
  secrets are no longer echoed in task output or logs.
- Added the `disable_tls_verification` option (default `false`) to keep
  certificate verification on by default while allowing an explicit opt-out.
- `afc_session` now fails gracefully on a failed login and reports a missing
  `pyafc` dependency via `missing_required_lib`.

### Bug Fixes
- Removed a duplicate AFC connection that ran before the `check_mode` guard in
  several modules, so `--check` no longer connects to AFC.

---

# v1.0.0

### Overview
This release introduces significant updates, including new features, enhancements, and bug fixes to the Ansible collection `arubanetworks.afc`. Below is a detailed summary of the changes.

---

### General Changes
- Updated copyright year across all files.
- Updated license from `GPL-2.0-or-later` to `GPL-3.0-or-later`.
- Updated collection description to "HPE Aruba Networking Fabric Composer collections".

---

### Enhancements and Features

#### Documentation Updates
- Improved documentation across all modules with better descriptions, examples, and structure.
- Added detailed examples for new operations and configurations, including:
  - Reapply operations for EVPN, VRF, Overlay, Underlay, and VSX.
  - Token-based authentication examples for all modules.
  - New configurations for SNMPv2c, SNMPv3, and Trap Servers.
  - Enhanced examples for DHCP Relay, DNS, and DSS configurations.

#### Module Enhancements
- **`afc_aaa`**:
  - Added support for token-based authentication.
  - Enhanced structure for `radius_data` with detailed suboptions.
- **`afc_dhcp_relay`**:
  - Added new options for `v4relay_option82_policy`, `v4relay_option82_validation`, and `v4relay_source_interface`.
  - Improved support for IPv6 DHCP server configurations.
- **`afc_discovery`**:
  - Enhanced `discovery_data` structure with additional options like `service_account_user`.
- **`afc_dns`**:
  - Added support for `domain_list` and `name_servers` configurations.
- **`afc_dss`**:
  - Added support for creating, updating, and deleting DSS objects like policies, rules, endpoint groups, qualifiers, and networks.
  - Introduced new suboptions for DSS configurations, including `priority`, `enforcers`, and `service_bypass`.
- **`afc_ports`**:
  - Added support for configuring LAG and VSX LAG.
  - Enhanced `ports_data` structure for physical and LAG configurations.
- **`afc_snmp`**:
  - Added support for SNMPv2c and SNMPv3 configurations with Trap Servers.
  - Improved examples for device-specific SNMP configurations.
- **`afc_vrf`**:
  - Added support for reapplying VRF configurations.
- **`afc_vsx`**:
  - Added support for reapplying VSX configurations.

#### New Features
- **Reapply Operations**:
  - Added support for reapplying configurations for EVPN, VRF, Overlay, Underlay, and VSX.
- **Token-Based Authentication**:
  - All modules now support token-based authentication for improved security and session reuse.
- **Enhanced Validation**:
  - Improved validation for input parameters across all modules.

---

### Bug Fixes
- Fixed inconsistencies in type hints and docstrings across modules.
- Resolved issues with response validation in HTTP requests.
- Addressed edge cases in switch and fabric management workflows.

---

### Breaking Changes
- Updated method signatures for several modules to improve clarity and maintainability.
- Some modules now require stricter type annotations, which may affect backward compatibility.

---

### Miscellaneous
- General code cleanup and refactoring for better readability and maintainability.
- Added `# noqa` comments to suppress specific linting warnings where necessary.

---

### Notes