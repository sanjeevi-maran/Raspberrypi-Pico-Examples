
import machine
from machine import ADC, Pin

import time

adc = ADC(Pin(26))

while True:

    a=adc.read_u16() #pot-0 to 65000
    print(a)
    if(a>60):
        print("high")
    else:
        print("low")
        
    time.sleep(1)