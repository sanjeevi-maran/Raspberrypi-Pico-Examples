;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; from machine import UART, Pin
import time



uart0 = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13)) #(0-port,baudrate,tx pin,rx pin)

while(1):
    
    txData = b'helo\r'
    
    uart0.write(txData)
    
    time.sleep(2)
    
    a ="acdefghijklmn"  
    
    #uart0.write(a.encode())
    
    uart0.write(a)
    
    time.sleep(2)
