AFC Ansible Collection
=========

This Ansible collection provides a set of platform dependent configuration management modules specifically designed for the Aruba Fabric Composer.

Requirements
------------

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
Downloading https://galaxy.ansible.com/download/arubanetworks-afc-0.0.1.tar.gz to /home/murali/.ansible/tmp/ansible-local-73666vlr4p5zw/tmp0gw8hrxz/arubanetworks-afc-0.0.1-vx5v8cw0
Installing 'arubanetworks.afc:0.0.1' to '/home/murali/.ansible/collections/ansible_collections/arubanetworks/afc'
arubanetworks.afc:0.0.1 was installed successfully
Skipping 'ansible.netcommon:2.3.0' as it is already installed
Skipping 'ansible.utils:2.3.1' as it is already installed
```

* **Change into the collections directory** where the AOS-CX Ansible collection (arubanetworks.aoscx) was installed.
    You can either execute `ansible-galaxy collection list` to find or use the following command:
    ```
    cd "$(ansible-galaxy collection list | grep -E '^#.*\.ansible' | sed 's/\# //')/arubanetworks/afc"
    ```
    * Example output of `ansible-galaxy collection list` and `cd` command:

    ```
	ansible-control-machine$ansible-galaxy collection list
	# /users/chiapuzi/.ansible/collections/ansible_collections
	Collection               Version
	------------------------ -------
	ansible.netcommon        2.3.0
	ansible.posix            1.1.1
	ansible.utils            2.3.1
	arubanetworks.afc        0.0.1
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
* Optional: Install pycurl
    Debian based distros:
    ```
    apt-get install curl openssl libcurl4-openssl-dev libssl-dev python3-dev
    ```
    Red Hat based distros:
    ```
    yum install curl openssl openssl-devel libcurl libcurl-devel python3-devel
    ```
    And install pycurl:
    ```
    python3 -m pip install pycurl
    ```

Inventory Variables
-------------------

The variables that should be defined in your inventory for your AOS-CX host are:

* `afc_ip`: IP address of Fabric Composer in `A.B.C.D` format.
* `afc_username`: Administrative username for AFC in `plaintext` format.
* `afc_password`: Administrative Password for AFC in `plaintext` format.
* `discovery_data`: A dictionary containing switch level `admin_passwd` and `afc_admin_passwd`.
* `devices_assignment`: A dictionary containing switch level role assignments with IP as key and role as value.

Example Playbooks
-----------------

### Including the Collection

If collection installed through Galaxy add `arubanetworks.afc` to your list of collections:

```yaml
- hosts: all
  collections:
    - arubanetworks.afc
  vars:
    ansible_python_interpreter: /usr/bin/python3
  gather_facts: False
  tasks:
  - name: Run discovery
    arubanetworks.afc.afc_run_discovery:
      afc_ip: 10.10.10.10
      afc_username: 'afc_admin'
      afc_password: 'afc_password'
      discovery_data:
        admin_passwd: 'switch_admin_password'
        afc_admin_passwd: 'afc_admin_password'
      devices_assignment:
        10.10.10.11: leaf
        10.10.10.12: leaf
```

Contribution
-------
At Aruba Networks we're dedicated to ensuring the quality of our products, so if you find any issues at all please open an issue on our [Github](https://github.com/aruba/afc-ansible-collection) and we'll be sure to respond promptly!

For more contribution opportunities follow our guidelines outlined in our [CONTRIBUTING.md](https://github.com/aruba/afc-ansible-collection/blob/master/CONTRIBUTING.md)

License
-------

Apache 2.0

Author Information
------------------
 - Arnaud Le Gall
 - Muralidhara Kakkunje
 - Rupali Ishwar Mali
