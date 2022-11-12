import time
from machine import Pin

led    = Pin(25, Pin.OUT)
#switch = Pin(0, Pin.IN)
switch = machine.Pin(0, Pin.IN, Pin.PULL_UP)

# For demo purposes, we have an infinite loop here
while True:
    
    time.sleep(2)
    a=switch.input()
    print(type(a))
    if(a==1):
        print("led on")
    else:
        print("led off")