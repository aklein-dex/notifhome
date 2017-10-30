import thread
from config import config
from gpio_manager import init_gpio_output, activate_gpio

# Gpio pin for the buzzer
PIN = config.PIN_BUZZER

# Sets the sleep duration between 2 beeps.
sleepTime = 0.5

# Set the number of beeps.
repetition = 10

def init_buzzer():
    """ Nothing special, just emit beep"""
    init_gpio_output("buzzer", PIN)
    emit_beep()
    return True

def emit_beep():
    """Start thread method to emit a beep"""
    try:
       thread.start_new_thread( activate_gpio, ("buzzer", sleepTime, repetition) )
    except:
       print "Error: unable to start thread"
      
