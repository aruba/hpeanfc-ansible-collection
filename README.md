HPEANFC Ansible Collection
=========

This Ansible collection provides a set of platform dependent configuration management modules specifically designed for the HPE Aruba Networking Fabric Composer.

Requirements
------------

* HPE ANFC 7.0/7.1 (6.x or 7.2+ unstable)
* Python 3 or later
* Ansible 2.10.5 or later
  * Refer to [Ansible's documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) for installation steps

Installation
------------

* Through Galaxy:

```
ansible-galaxy collection install arubanetworks.afc
```

* Example Output:
```
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/download/arubanetworks-afc-1.0.0.tar.gz to /home/murali/.ansible/tmp/ansible-local-73666vlr4p5zw/tmp0gw8hrxz/arubanetworks-afc-1.0.0-vx5v8cw0
Installing 'arubanetworks.afc:1.0.0' to '/home/murali/.ansible/collections/ansible_collections/arubanetworks/afc'
arubanetworks.afc:1.0.0 was installed successfully
Skipping 'ansible.netcommon:2.3.0' as it is already installed
Skipping 'ansible.utils:2.3.1' as it is already installed
```

* **Change into the collections directory** where the HPE Aruba Networking Fabric Composer Ansible collection (arubanetworks.afc) was installed.
    You can either execute `ansible-galaxy collection list` to find or use the following command:
    ```
    cd "$(ansible-galaxy collection list | grep -E '^#.*\.ansible' | sed 's/\# //')/arubanetworks/afc"
    ```
    * Example output of `ansible-galaxy collection list` and `cd` command:

    ```
  ansible-control-machine$ansible-galaxy collection list
  # /users/murali/.ansible/collections/ansible_collections
  Collection               Version
  ------------------------ -------
  ansible.netcommon        2.3.0
  ansible.posix            1.1.1
  ansible.utils            2.3.1
  arubanetworks.afc        1.0.0
  ```
    
* Install all Ansible requirements, with the following command:
    ```
    ansible-galaxy install -r requirements.yml
    ```
* Install all Python requirements with the following command:
    ```
    python3 -m pip install -r requirements.txt
    ```
* **Change back** into your working directory and begin automating!
  ```
  ansible-control-machine$cd /users/murali/sandbox/
  ```

Inventory Variables
-------------------

For authentication users have two options, either through a generated authentication token or through supplying the username and password to your HPE ANFC instance.

The bare minimum variables that should be defined in your inventory for your HPE ANFC host are:

* `afc_ip`: IP address of Fabric Composer in `A.B.C.D` or FQDN format.
* `afc_username`: Administrative username for HPEANFC in `plaintext` format.
* `afc_password`: Administrative Password for HPEANFC in `plaintext` format.
* `auth_token`: Authentication token generated using API endpoint [`/auth/token`](https://developer.arubanetworks.com/aruba-fabric-composer/reference/getapikey-1)  - for detailed instructions see [Getting Started with the HPE ANW Fabric Composer API Authentication.](https://developer.arubanetworks.com/aruba-fabric-composer/docs/getting-started-with-the-afc-api#api-authentication) Required if `afc_username` and `afc_password` are not provided.


Rest of the variables are are explained in [docs](docs) section with examples.

Example Playbooks
-----------------

### Including the Collection

If collection installed through Galaxy add `arubanetworks.afc` to your list of collections:

```yaml
- hosts: all
  collections:
    - arubanetworks.afc
  gather_facts: False
  tasks:
    - name: Day0 | Discovery | Discover switches with IP address
      arubanetworks.afc.afc_discovery:
        afc_ip: "{{ afc_ip }}"
        afc_username: "{{ afc_username }}"
        afc_password: "{{ afc_password }}"
        data:
          admin_passwd: "admin"
          afc_admin_passwd: "aruba"
          switches:
              - 10.156.11.166
              - 10.156.14.253
              - 10.156.11.255
              - 10.156.19.167
              - 10.156.15.109
              - 10.156.18.255
```

### Making use of afc_session module to generate an auth_token and reusing the same token for subsequent actions.

The modules are designed to close the session for every username/password based action. In case we wish to re-use the session, the playbooks should only be receiving the auth_token as input var. If username and password are also sent along with the auth_token, the modules would assume that username and password combination was used and the session would get closed as a precautionary measure. This results in subsequent tasks to fail. Hence, the username and password should only be used with afc_session module and remaining playbooks should only get auth_token as input and should never be given username and password as input along with the auth_token.

```yaml
- hosts: all
  collections:
    - arubanetworks.afc
  gather_facts: False
  tasks:
    - name: Create Session
      arubanetworks.afc.afc_session:
        afc_ip: "10.10.10.10"
        afc_username: "afc_admin"
        afc_password: "afc_password"
      register: reg_afc_instance

    - name: Capture the auth_token
      ansible.builtin.set_fact:
        auth_token: "{{ reg_afc_instance['auth_token'] }}"

    - name: Day0 | Discovery | Discover switches with IP address
      arubanetworks.afc.afc_discovery:
        afc_ip: "10.10.10.10"
        auth_token: "{{ auth_token }}"
        data:
          admin_passwd: "admin"
          afc_admin_passwd: "aruba"
          switches:
              - 10.156.11.166
              - 10.156.14.253
              - 10.156.11.255
              - 10.156.19.167
              - 10.156.15.109
              - 10.156.18.255
```

Contribution
-------
At HPE Aruba Networking we're dedicated to ensuring the quality of our products, so if you find any issues at all please open an issue on our [GitHub](https://github.com/aruba/hpeanfc-ansible-collection) and we'll be sure to respond promptly!

For more contribution opportunities follow our guidelines outlined in our [CONTRIBUTING.md](https://github.com/aruba/hpeanfc-ansible-collection/blob/master/CONTRIBUTING.md)

License
-------

Apache 2.0

Author Information
------------------
 - Arnaud Le Gall
 - Muralidhara Kakkunje
 - Rupali Ishwar Mali
