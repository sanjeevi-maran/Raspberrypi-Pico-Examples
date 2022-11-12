import time
from machine import Pin

led = Pin(25, Pin.OUT)

# For demo purposes, we have an infinite loop here
while True:
    led.high()
    time.sleep(0.5)
    print("led high")
    led.low()
    time.sleep(0.5)
    print("led low")