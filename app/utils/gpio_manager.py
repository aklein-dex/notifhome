import onionGpio
import time

gpio_buzzer = None
gpio_led = None

def init_gpio_output(element, pin):
    """Initialize the gpio."""
    if element == "led":
        global gpio_led
        gpio_led = onionGpio.OnionGpio(pin)
        # set to output direction with zero (LOW) being the default value
        gpio_led.setOutputDirection(0)
    else:
        global gpio_buzzer
        gpio_buzzer = onionGpio.OnionGpio(pin)
        # set to output direction with zero (LOW) being the default value
        gpio_buzzer.setOutputDirection(0)
 
    return True

def activate_gpio(element, sleepTime, repetition):
    """ Send current."""
     
    # create a variable to hold the value of the LED
    ledValue = 1
    
    count = 0

    while count < repetition:
        # set the GPIO's value
        # note: I wanted to do this "if" outside the loop but
        #       I can't figure out how to do it...
        if element == "led":
            global gpio_led
            gpio_led.setValue(ledValue)
        else:
            global gpio_buzzer
            gpio_buzzer.setValue(ledValue)

        # flip the value variable
        if ledValue == 1:
            ledValue = 0
        else:
            ledValue = 1

        # make the program pause
        time.sleep(sleepTime)
        count = count + 1
