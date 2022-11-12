
import machine
from machine import ADC, Pin

import time

x = ADC(Pin(26))
y = ADC(Pin(27))
z = ADC(Pin(28))

while True:

    x_axis=int((x.read_u16()/1000)/10)#pot-0 to 65000
    y_axis=int((y.read_u16()/1000)/10)
    z_axis=int((z.read_u16()/1000)/10)
    
    print("**************")
    
    print(x_axis)
    print(y_axis)
    print(z_axis)
    
    if(x_axis ==3 and y_axis==3 and z_axis==3):
        print("Normal")
    else:
        print("fall detection")
    
    print("**************")

        
    time.sleep(0.5)