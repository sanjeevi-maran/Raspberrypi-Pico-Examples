import time
from machine import Pin, PWM


pwm = PWM(Pin(16))

pwm.freq(1000)

#pwm duty high 65025
#pwm duty low  0
#pwm.duty_u16(duty)

while True:
    
            pwm.duty_u16(65025)
            time.sleep(2)
            pwm.duty_u16(55025)
            time.sleep(2)
            pwm.duty_u16(45025)
            time.sleep(2)
            pwm.duty_u16(35025)
            time.sleep(2)
            pwm.duty_u16(25025)
            time.sleep(2)
            pwm.duty_u16(15025)
            time.sleep(2)
            pwm.duty_u16(5025)
            time.sleep(2)
            pwm.duty_u16(0)
            time.sleep(2)

            
