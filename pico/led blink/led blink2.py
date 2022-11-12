import time
from machine import Pin 

led    = Pin(25, Pin.OUT)
#switch = Pin(0, Pin.IN)


# For demo purposes, we have an infinite loop here
while True:
    
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)