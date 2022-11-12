from machine import UART, Pin
import time

uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

time.sleep(0.1)

while(1):
    
    receiving_data = " "
    rxData = " "
    
    while uart0.any() > 0:          
        rxData = uart0.read()
        
    try:
        receiving_data = rxData.decode('utf-8')
        data_len = len(receiving_data)
        #print(receiving_data)
        receiving_data = int(receiving_data[2:data_len-3])  #   *+00010#        -total 8 , length 8, skip  position from begining  00010# ,234567 - 00010,     
        print(receiving_data)
        time.sleep(2)
        
        
        if(receiving_data > 100):
            print("HIGH")
        else:
            print("LOW")
        
        #uart0.flushInput()
        
    except:
        pass