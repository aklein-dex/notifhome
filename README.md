# notifhome
Minimalist python Web server (using [bottle](https://bottlepy.org/)) to manage notifications 
with the [Onion Omega2](https://onion.io/) board.

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

When I'm outside and try to contact my wife (or the opposite) on her cellphone, 
she sometimes doesn't hear her phone ringing because she is in another room or her phone is in vibration mode in her bag. 

#### Solution

With this project, I'm able to send notifications to the Omega2 so it will turn on the LED, 
emit a beep and show a message on the screen.

To aknowledge the notification the user can push a button (attached to the Omega2) or 
log in to the server and disable the notification.

############ GET CERTIFICATE FOR HTTPS

### Instructions

#### Install git (optional)

Git takes 6.8M of disk space. You may want to clone this repo on your PC and transfer
the files (scp) if you don't want to install git.

```
$ opkg update
$ opkg install git git-http ca-bundle
$ git --version
git version 2.11.0
```

#### Install python 3

It will take 3.4M + 7.4M of disk space.

```
$ opkg update
$ opkg install python3-light
$ opkg install python3-pip
# when using pip you may encounter a small configuration issue with the setuptools module and can be easily fixed:
$ pip3 install --upgrade setuptools
```

#### Install bottle

[Bottle](https://bottlepy.org/docs/dev/) is a fast, simple and lightweight WSGI micro web-framework.
[Beaker](https://github.com/bottlepy/bottle-beaker) is session and caching library with WSGI Middleware.

It will take 0.2M + 0.2M.

```
$ pip3 install bottle
$ pip3 install bottle-beaker
```

I wanted to use [Cork](http://cork.firelet.net/) for authentication and authorization but to install it
it needs to compile some C code. Installing a C compiler on the Omega is not that easy, so instead
I'll handle authentication and authorization by myself.


#### Run the server

Simply run the command:
```
$ python startup.py
```
Open your browser to http://localhost:9090/. The default login/pwd is admin/admin.


### Future version

#### Version 2

Multiple boards will be connected together. There will be 1 master and multiple slaves (placed in different rooms). 
A user connects to the master to send a notification and the notifications propagate to all the slaves.

#### Version 3

In case the slaves are located far away from the WiFi router, they will be able to connect to the master hotspot.
