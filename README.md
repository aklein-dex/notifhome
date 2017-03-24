# notifhome
Minimalist python Web server to manage notifications with the Onion Omega2 board.

https://onion.io/

https://bottlepy.org/

I didn't receive the Omega2 yet, but here is the steps to setup bottle on a VM.
I'll update this page once I have the Omega2.

### Install python

```
opkg install python-light
opkg install pip (?)
```

### Install bottle

```
$ pip install bottle
$ pip install bottle-cork
$ pip install bottle-beaker
```

### Setup

After cloning the repo, run this command to create the database:
```
$ pythom migrate.py init
```

### Run the server

Simply run the command:
```
$ python notifhome.py
```
Open your browser to http://localhost:9090/. The default login/pwd is admin/admin.
