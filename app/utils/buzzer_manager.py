import thread
from config import config
from gpio_manager import init_gpio_buzzer, activate_gpio_buzzer

PIN = config.PIN_BUZZER

# specify sleep duration
sleepTime = 0.5

repetition = 10


def init_buzzer():
    """ Nothing special, just emit beep"""
    init_gpio_buzzer(PIN)
    emit_beep()
    return True

def emit_beep():
    try:
       thread.start_new_thread( activate_gpio_buzzer, (sleepTime, repetition) )
    except:
       print "Error: unable to start thread"
      
