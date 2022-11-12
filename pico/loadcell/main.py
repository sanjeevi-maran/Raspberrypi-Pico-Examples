from machine import freq
freq(160000000)
from hx711 import HX711


while(1):
    driver = HX711(d_out=4, pd_sck=5)
    driver.channel=HX711.CHANNEL_A_64
    driver.channel
    a=int(abs(driver.read())/10000)-13
    print(a)
    
    a=a*500 #(500 gram)
    
    driver.power_off()
