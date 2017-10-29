import thread
from config import config
from gpio_manager import init_gpio_led, activate_gpio_led

PIN = config.PIN_LED

# specify sleep duration
sleepTime = 0.5

repetition = 10


def init_led():
    """ Nothing special, just blink the led"""
    init_gpio_led(PIN)
    blink_led()
    return True

def blink_led():
    try:
       thread.start_new_thread( activate_gpio_led, (sleepTime, repetition) )
    except:
       print "Error: unable to start thread"

