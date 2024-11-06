AFC Ansible Collection
=========

Below steps are only needed until the arubanetworks.afc collection is published.

Create and install the ansible collection in the environment using git repo contents.
------------

Clone the Git repository
```bash
$ git clone git@github.hpe.com:GSE/ArubaAFC-ansible.git
```

Install required Python packages
```bash
$ cd ArubaAFC-ansible/
$ pip install -r requirements.txt
```

Build collection using the directory content
```bash
$ ansible-galaxy collection build
```

Install ansible collection using the created tar.gz file within the same directory
```bash
$ ansible-galaxy collection install arubanetworks-afc-1.0.0.tar.gz
```
