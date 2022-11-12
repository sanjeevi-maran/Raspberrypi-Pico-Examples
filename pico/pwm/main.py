import time
from machine import Pin, PWM


pwm = PWM(Pin(16))

pwm.freq(1000)

while True:
    
    print("pwm")
    
    for duty in range(65025):
            #print(duty)
            pwm.duty_u16(duty)
            time.sleep(0.0001)
    for duty in range(65025, 0, -1):
            #print(duty)
            pwm.duty_u16(duty)
            time.sleep(0.0001)
