## Build L2TP over IPSec VPN for Ubuntu 16.04

### Step 1: Access your server

* Copy this directory to your server (you may use scp or git clone)

* Make sure you are in root bash (sudo -s)

### Step 2: Setup basic configure

* Edit the file `ipsec.conf` at line 22 (left=x.x.x.x): change x.x.x.x to your server public network ip 

* [Optional] edit the file `options.xl2tpd`, change `ms-dns ip` to match client laptop DNS (default is great)

* Run the command `source pkg_install`

### Step 4: Setup your shared password

* Edit `/etc/ipsec.secrets` to add your password

* Text format: `%any : PSK <Your Password>`, where `<Your Password>` should be replaced by your new password

### Step 5: Setup user information

* Edit `/etc/ppp/chap-secrets` to add user account and password

* Text format: `<User Name> l2tpd <User Password> *`, where `*` denotes this user can use all ip address

### Step 6: Final start

* Run the command `source start`

### Congradulations

* Now VPN should work. You can try to connect this VPN on your laptop

* If connect failed, please check the DNS on your laptop: add 192.168.1.1 or 192.168.1.2

* Or you can change the file `/etc/ppp/options.xl2tpd` ms-dns to match your DNS and re-run Step 6