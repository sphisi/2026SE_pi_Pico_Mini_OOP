





from machine import Pin
from time import sleep, time

class Led_lights(Pin):
    #inhereitance using Pin class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        #defines state
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        #overirde polymorphism of class 
        self.high()
        if self.__debug:
            print(f"LED connected to {self.__pin} is on")

    def off(self):
        #overide polymorphism of class for off
        self.low()
        if self.__debug:
            print(f"LED connected to {self.__pin} is off")

    def toggle(self):
        #overide polymorphism of class for toggle
        if self.value() == 0:
            self.on()
        elif self.value ==1:
            self.off()

    @property
    def led_light_state(self):
        #overloading
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self):
    #overloading
        if value == 1:
            self.on()
        elif value == 0:
            self.off()


red_light = Led_lights(3, False, True)

while True:
    red_light.toggle()
    print(red_light.led_light_state)
    sleep(1)