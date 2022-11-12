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
        print(receiving_data,len(receiving_data))      
    except:
        pass
    
    if(receiving_data == '1'):
        print(" motor on ")
    else:
        print("motor off")