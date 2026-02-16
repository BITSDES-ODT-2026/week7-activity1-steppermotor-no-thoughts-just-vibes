from machine import Pin
import time
s1=Pin(4,Pin.OUT)
s2=Pin(14,Pin.OUT)
s3=Pin(18,Pin.OUT)
s4=Pin(19,Pin.OUT)
lis=[s1,s2,s3,s4]
while True:
    s1.value(1)
    s2.value(0)
    s3.value(0)
    s4.value(0)
    time.sleep_ms(50)

    s1.value(0)
    s2.value(1)
    s3.value(0)
    s4.value(0)
    time.sleep_ms(50)

    s1.value(0)
    s2.value(0)
    s3.value(1)
    s4.value(0)
    time.sleep_ms(50)

    s1.value(0)
    s2.value(0)
    s3.value(0)
    s4.value(1)
    time.sleep_ms(50)
    
    
    s1.value(0)
    s2.value(0)
    s3.value(1)
    s4.value(0)
    time.sleep_ms(50)

    s1.value(0)
    s2.value(1)
    s3.value(0)
    s4.value(0)
    time.sleep_ms(50)

    
