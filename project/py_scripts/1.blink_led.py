from machine import Pin
from time import sleep

#ready time
sleep(0.1)

#desired output pin
led_pin = 25

#configure pin as an output and create led object for pin class
led = Pin(led_pin, Pin.OUT)

while True:
    led.value(True)
    sleep(1)
    led.value(False)
    sleep(1)