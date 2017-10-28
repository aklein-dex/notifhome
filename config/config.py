import ConfigParser

defaults = {
    "logfile": "notifhome.log",
    "port": "80",
    "host": "0.0.0.0",
    "date_format": "%b %d, %H:%M",
    "users_file": "config/users.authz",
    "queue_folder": "queue",
    "screen": "True",
    "button": "True",
    "buzzer": "True",
    "led": "True",
    "pin_buzzer": "0",
    "pin_led": "2",
    "pin_button": "12"
   }
   
config = ConfigParser.RawConfigParser(defaults)
config.read('config/myconfig.local')

section = 'notifhome'

LOGFILE      = config.get(section, 'logfile')
PORT         = config.getint(section, 'port')
HOST         = config.get(section, 'host')
DATE_FORMAT  = config.get(section, 'date_format')
USERS_FILE   = config.get(section, 'users_file')
QUEUE_FOLDER = config.get(section, 'queue_folder')
SCREEN       = config.getboolean(section, 'screen')
BUTTON       = config.getboolean(section, 'button')
BUZZER       = config.getboolean(section, 'buzzer')
LED          = config.getboolean(section, 'led')
PIN_BUZZER   = config.getint(section, 'pin_buzzer')
PIN_LED      = config.getint(section, 'pin_led')
PIN_BUTTON   = config.getint(section, 'pin_button')

