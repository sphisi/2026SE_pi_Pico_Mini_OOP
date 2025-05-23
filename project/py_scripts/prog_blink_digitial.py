from machine import Pin
from time import sleep

#ready time
sleep(0.1)

#desired output pin
led_pin = 25
led2_pin = 15
#data_pin = 13

#configure pin as an output and create led object for pin class
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

#configure input pin
#data = Pin(data_pin, Pin.IN)

while True:
    #if data.value() == 1:
    led.value(True)
    led2.value(False)
    sleep(1)
    #else:
    led2.value(True)
    led.value(False)
    