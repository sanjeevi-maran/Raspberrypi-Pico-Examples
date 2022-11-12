import time
from machine import Pin

#led    = Pin(25, Pin.OUT)
#switch = Pin(0, Pin.IN)

#switch = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

switch = machine.Pin(0, machine.Pin.IN)  #pin numer , input

# For demo purposes, we have an infinite loop here

while True:
    
    time.sleep(2)
    
    a=switch.value() #read = values
    
    #print(type(a))
    
    if(a==1):
        print("led on")
    else:
        print("led off")
    