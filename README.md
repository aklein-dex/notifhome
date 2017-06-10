# notifhome
Minimalist python Web server (using [bottle](https://bottlepy.org/)) to manage notifications with the [Onion Omega2](https://onion.io/) board.

*I received the board (see image) and will soon start to work on it and update the instructions below.*

### Components

- Omega2
- expansion dock
- proto expansion
- OLED screen
- LED
- buzzer
- button

### Scenario

#### Problem

When I'm outside and try to contact my wife (or the opposite) on her cellphone, she sometimes doesn't hear her phone ringing because she is in another room or her phone is in vibration mode in her bag. 

#### Solution

With this project, I'm able to send notifications to the Omega2 so it will turn on the LED, emit a beep and show a message on the screen.

To aknowledge the notification the user can push a button (attached to the Omega2) or log in to the server and disable the notification.

### Instructions

#### Install python

```
opkg install python-light
opkg install pip (?)
```

#### Install bottle

```
$ pip install bottle
$ pip install bottle-cork
$ pip install bottle-beaker
```

#### Setup

After cloning the repo, run this command to create the database:
```
$ pythom migrate.py init
```

#### Run the server

Simply run the command:
```
$ python notifhome.py
```
Open your browser to http://localhost:9090/. The default login/pwd is admin/admin.


### Future version

#### Version 2

Multiple boards will be connected together. There will be 1 master and multiples slaves (placed in different rooms). A user connects to the master to send a notification and the notifications propagate to all the slaves.

#### Version 3

In case the slaves are located far away from the WiFi router, they will be able to connect to the master hotspot.
