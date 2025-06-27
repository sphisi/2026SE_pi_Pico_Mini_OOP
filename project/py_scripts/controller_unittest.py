import controller

debug = True

red_light = controller.Led_light(3, False, debug)
amber_light = controller.
green_light = controller.

ped_red_led = controller.
ped_green_led = controller.

button = controller.
buzzer = controller.

while True:
    controller.update()
    sleep(0.1)