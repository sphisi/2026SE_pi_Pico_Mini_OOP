from led_light import led_light
from machine import Pin
from time import sleep

red_car_led = led_light(3, False)
orange_car_led = led_light(4, False)
green_car_led = led_light(5, False)

sleep(1)

print("testing leds and state")
for i in range(3):
    #toggle each in a row
    green_car_led.off()
    red_car_led.on()
    print(f"red light is {red_car_led.led_light_state}")
    sleep(2)
    red_car_led.off()
    orange_car_led.on()
    print(f"orange light is {orange_car_led.led_light_state}")
    sleep(2)
    orange_car_led.off()
    green_car_led.on()
    print(f"green light is {green_car_led.led_light_state}")
    sleep(2)

print("LED testign complete")