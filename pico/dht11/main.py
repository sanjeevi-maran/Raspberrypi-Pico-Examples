from machine import Pin
import utime

from dht import DHT11, InvalidChecksum


# Wait 1 second to let the sensor power up
utime.sleep(1)

pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)

sensor = DHT11(pin)

try:

    T=sensor.temperature
    h=sensor.humidity
    print(T)
    print(h)
    if(T>50):
        print("temp high")
    else:
        print("temp low")
    
except InvalidChecksum:
    print("Checksum from the sensor was invalid")