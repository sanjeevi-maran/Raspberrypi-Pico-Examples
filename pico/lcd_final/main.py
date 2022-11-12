from lcd import LCD
import utime


lcd = LCD()

lcd.print1('Temperature:',1,0) #first row -  1-common - 0 -position

lcd.print2('hi',1,11)           #second row

utime.sleep(1)




