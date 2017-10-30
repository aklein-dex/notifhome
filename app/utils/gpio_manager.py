import onionGpio
import time

gpio_buzzer = None
gpio_led = None

def init_gpio_output(element, pin):
    """Initialize the gpio."""
    if element == "led":
        global gpio_led
        gpio = gpio_led
    else:
        global gpio_buzzer
        gpio = gpio_buzzer
        
    # instantiate a GPIO object
    gpio = onionGpio.OnionGpio(pin)
    # set to output direction with zero (LOW) being the default value
    gpio.setOutputDirection(0)
    return True

def activate_gpio(element, sleepTime, repetition):
    """ Send current."""
    if element == "led":
        global gpio_led
        gpio = gpio_led
    else:
        global gpio_buzzer
        gpio = gpio_buzzer
        
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
