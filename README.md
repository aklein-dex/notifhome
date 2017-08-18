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

#### Source code

##### Install git (optional)

Git takes 6.8M of disk space. 

```
$ opkg update
$ opkg install git git-http ca-bundle
$ git --version
git version 2.11.0
```
##### Transfer the file

You may want to clone this repo on your PC and transfer
the files (scp) if you don't want to install git.

#### Install python

It will take 3.4M of disk space.

```
$ opkg update
$ opkg install python-light pyOledExp
```

#### Setup

##### Config

Open the file config/myconfig.py and set the approriate values depending of your system.

##### Users

Edit the file config/users.authz to add users. The format is <username>:<password>.

#### Run the server

Simply run the command:
```
$ python startup.py
```
Open your browser to http://localhost:9090/.


### Future version

#### Version 2

Multiple boards will be connected together. There will be 1 master and multiple slaves (placed in different rooms). 
A user connects to the master to send a notification and the notifications propagate to all the slaves.

#### Version 3

In case the slaves are located far away from the WiFi router, they will be able to connect to the master hotspot.
