import thread
from config import config
from gpio_manager import init_gpio_output, activate_gpio

# Gpio pin for the led
PIN = config.PIN_LED

# Sets the sleep duration between 2 blinks.
sleepTime = 0.5

# Set the number of beeps.
repetition = 10

def init_led():
    """ Nothing special, just blink the led"""
    init_gpio_output("led", PIN)
    blink_led()
    return True

def blink_led():
    """Start thread method to blink the led."""
    try:
       thread.start_new_thread( activate_gpio, ("led", sleepTime, repetition) )
    except:
       print "Error: unable to start thread"

