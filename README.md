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
- resistors 51kΩ, 5.1kΩ, 200Ω, 200Ω
- capacitor 100nF
- jumper wires

### Scenario

#### Problem

When I'm outside and try to contact my wife on her cellphone, 
she sometimes doesn't hear it ringing because she is in another room or it is in vibration mode in her bag. 

#### Solution

With this project, I'm able to send messages to the Omega2 to notify my wife. The Omega2 will turn on the LED, 
emit a beep and show a message on the screen.

To acknowledge a notification, simply press the button on the Omega2 or use the Website.

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
##### Transfer this project

After installing `git`, just clone this repository.

Or you may want to clone this repository on your PC and transfer 
the files to the Omega2 using `scp` if you don't want to install `git`.

#### Install python

It will take 7.7M of disk space.

```
$ opkg update
$ opkg install python-light python-email python-logging python-codecs python-openssl pyOledExp pyOnionGpio
```

Note: we are using python 2.7 because of pyOledExp.

#### Setup

##### Config

Default values are in `config/config.py` but do not modify this file. Instead, create another file `config/myconfig.local` 
to override the default values.
The file `config/myconfig.local` is not versioned, so there is no risk to lose it when updating the repository.
Make sure to start the file with `[notifhome]`. Here is an example:
```
[notifhome]
host = 127.0.0.1
port = 8080
screen = False
buzzer = True
```

##### Users

Edit the file `config/users.authz` to add users. The format is `{username}:{password}`.

#### Run the server

Simply run the command:
```
$ python startup.py
```
Open your browser to `http://localhost:9090/`.

#### Tests

The package [WebTest](https://docs.pylonsproject.org/projects/webtest/en/latest/) is required to run the tests. 
I don't run the tests on the Omega2 because the disk space is limited, so I only run the tests on my computer.
```
$ pip install WebTest
$ python test/test_notifhome.py
```

### Future version

#### Version 2

Multiple boards will be connected together. There will be 1 master and multiple slaves (placed in different rooms). 
A user connects to the master to send a notification and the notifications propagate to all the slaves.

#### Version 3

In case the slaves are located far away from the WiFi router, they will be able to connect to the master hotspot.
