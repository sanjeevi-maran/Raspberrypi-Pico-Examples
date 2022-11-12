from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# or uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

#phone call
def call():

        txData = 'AT\r'

        time.sleep(5)

        uart1.write(txData)

        txData ='ATD8754090958;\r'   #for call

        uart1.write(txData)

        time.sleep(20)

def message():

        txData = 'AT\r'

        time.sleep(0.5)

        uart1.write(txData)

        txData ='AT+CMGF=1\r'   #for call

        uart1.write(txData)

        time.sleep(0.5)

        txData ='AT+CMGS=\"8754090958\"\r'   #for call

        uart1.write(txData)

        time.sleep(0.5)

        txData ='HI\r'   #for call

        uart1.write(txData)

        time.sleep(0.5)

        uart1.write(str.encode(chr(26)))
        
message()
