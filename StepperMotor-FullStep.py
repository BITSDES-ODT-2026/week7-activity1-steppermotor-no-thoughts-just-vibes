from machine import Pin
import time    
s1=Pin(4,Pin.OUT)
s2=Pin(14,Pin.OUT)
s3=Pin(18,Pin.OUT)
s4=Pin(19,Pin.OUT)
lit=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
while True:
    for i in lit:
        s1.value(i[0])
        s2.value(i[1])
        s3.value(i[2])
        s4.value(i[3])
