from machine import Pin
from time import sleep, time

class led_light(Pin):
    #inhereitance using Pin class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        #defines state
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

    def on(self):
        #overirde polymorphism of class 
        self.high()
        if self.__debug:
            print(f"LED connected to {self.__pin} is {self.led_light_state}")

    def off(self):
        #overide polymorphism of class for off
        self.low()
        if self.__debug:
            print(f"LED connected to {self.__pin} is {self.led_light_state}")

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
    def led_light_state(self, value):
    #overloading
        if value == 1:
            self.on()
        elif value == 0:
            self.off()

    def flash(self):
        #non-blcing flash: toggle led every 0.5s 
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now