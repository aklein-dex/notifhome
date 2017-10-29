import onionGpio
import time

gpio_buzzer = onionGpio.OnionGpio(0)
gpio_led = onionGpio.OnionGpio(2)

def init_gpio_buzzer(pin):
    """ Nothing special, just blink the led"""
    global gpio_buzzer
    init_gpio_output(pin, gpio_buzzer)
    return True
    
def init_gpio_led(pin):
    """ Nothing special, just blink the led"""
    global gpio_led
    init_gpio_output(pin, gpio_led)
    return True

def init_gpio_output(pin, gpio):
    # instantiate a GPIO object
    gpio = onionGpio.OnionGpio(pin)
    # set to output direction with zero (LOW) being the default value
    gpio.setOutputDirection(0)
    return True

def activate_gpio_led(sleepTime, repetition):
    global gpio_led
    activate_gpio(gpio_led, sleepTime, repetition)

def activate_gpio_buzzer(sleepTime, repetition):
    global gpio_buzzer
    activate_gpio(gpio_buzzer, sleepTime, repetition)


def activate_gpio(gpio, sleepTime, repetition):
    """ Blink led for a period of time"""
    # create a variable to hold the value of the LED
    ledValue = 1
    
    count = 0

    while count < repetition:
        # set the GPIO's value
        gpio.setValue(ledValue)

        # flip the value variable
        if ledValue == 1:
            ledValue = 0
        else:
            ledValue = 1

        # make the program pause
        time.sleep(sleepTime)
        count = count + 1
