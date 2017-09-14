import os.path

# DO NOT MODIFY THIS FILE!
# If you want to change default values below, then create a 
# file "config/myconfig.local".

LOCAL_CONFIG="config/myconfig.local"

if os.path.isfile(LOCAL_CONFIG):
    with open(LOCAL_CONFIG, "r") as lines:
        array = []
        for line in lines:
            split = line.split("=")
            if split[0] == "PORT":
                PORT = split[1]
            elif split[0] == "HOST":
                HOST = split[1]
            elif split[0] == "DATE_FORMAT":
                DATE_FORMAT = split[1]
            elif split[0] == "USERS_FILE":
                USERS_FILE = split[1]
            elif split[0] == "QUEUE_FOLDER":
                QUEUE_FOLDER = split[1]
            elif split[0] == "SCREEN":
                SCREEN = split[1]
            elif split[0] == "BUTTON":
                BUTTON = split[1]
            elif split[0] == "SOUND":
                SOUND = split[1]
            elif split[0] == "LIGHT":
                LIGHT = split[1]
            elif split[0] == "PIN_SOUND":
                PIN_SOUND = split[1]
            elif split[0] == "PIN_LIGHT":
                PIN_LIGHT = split[1]
            elif split[0] == "PIN_BUTTON":
                PIN_BUTTON = split[1]

try:
    LOGFILE
except NameError:
    LOGFILE = "notifhome.log"

# Port to run the server
try:
    PORT
except NameError:
    PORT = 9090

# Host to run the server
try:
    HOST
except NameError:
    HOST = '0.0.0.0'
    
# Format use to display the date on the screen
try:
    DATE_FORMAT
except NameError:    
    DATE_FORMAT = "%b %d, %H:%M"

# File containing the list of users
try:
    USERS_FILE
except NameError:
    USERS_FILE = "config/users.authz"

# Folder containing unread notifications.
# In this folder, 1 file is 1 notification.
# When a notification is read, then the file is deleted.
try:
    QUEUE_FOLDER
except NameError:
    QUEUE_FOLDER = "queue"

# Enable/disable screen notifications 
try:
    SCREEN
except NameError:
    SCREEN = True

# Enable/disable sound notifications 
try:
    SOUND
except NameError:
    SOUND = True
    
# Enable/disable light notifications 
try:
    LIGHT
except NameError:
    LIGHT = True

# If a button is present. Otherwise user has to delete notifications
# via the Web site.
try:
    BUTTON
except NameError:
    BUTTON = True
    
# GPIO pin for the buzzer
try:
    PIN_SOUND
except NameError:
    PIN_SOUND = 0

# GPIO pin for the LED
try:
    PIN_LIGHT
except NameError:
    PIN_LIGHT = 2

# GPIO pin for the button
try:
    PIN_BUTTON
except NameError:
    PIN_BUTTON = 12
