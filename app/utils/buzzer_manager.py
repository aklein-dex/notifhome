import onionGpio
import time
from config import config

PIN = config.PIN_BUZZER

# specify sleep duration
sleepTime = 0.5

# instantiate a GPIO object
gpio_buzzer = onionGpio.OnionGpio(PIN)
# set to output direction with zero (LOW) being the default value
gpio_buzzer.setOutputDirection(0)


def init_buzzer():
    """ Nothing special, just emit beep"""
    emit_beep()
    return True
    
def emit_beep():
    """ Emit beep for a period of time"""
    # create a variable to hold the value of the buzzer
    buzzerValue = 1
    
    count = 0

    # TODO: a thread?
    while count < 6:
        # set the GPIO's value
        gpio_buzzer.setValue(buzzerValue)

        # flip the value variable
        if buzzerValue == 1:
            buzzerValue = 0
        else:
            buzzerValue = 1

        # make the program pause
        time.sleep(sleepTime)
        count = count + 1
