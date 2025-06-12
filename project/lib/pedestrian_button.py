from machine import Pin
from time import ticks_ms, ticks_diff, time

class Pedestrian_Button(Pin):
    #inherits pin attributes
    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  #track when last press
        self.__pedestrian_waiting = False
        self.button_state
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    #getter
    @property
    def button_state(self):
        if self.__debug:
            print(f"button connected to pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'Not Waiting'}")
        return self.__pedestrian_waiting
    
    #setter
    @button_state.setter
    def button_state(self, value):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f"Button state on Pin {self.__pin} set to {value}")

    def callback(self, pin):
        current_time = time.ticks_ms() #get time in ms
        if (time.ticks_diff(current_time, self.__last_pressed) > 200): #200ms delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")


        

    
