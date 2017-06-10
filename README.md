# notifhome
Minimalist python Web server (using [bottle](https://bottlepy.org/)) to manage notifications with the [Onion Omega2](https://onion.io/) board.

*I received the board (see image) and will soon start to work on it and update the instructions below.*

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
