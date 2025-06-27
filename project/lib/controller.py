from led_light import Led_light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSubsystem:
    def __init__(self, red, amber, green, debug=False):
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        if self.__debug:
            print("traffic light : Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        if self.__debug:
            print("traffic light : Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        if self.__debug:
            print("traffic light : Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()

class PedestrianSubsystem:
    def __init__(self, red, green, button, buzzer, debug=False):
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        if self.__debug:
            print("pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        if self.__debug:
            print("pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()

    def show_warning(self):
        if self.__debug:
            print("pedestrian: Red Flashing")
        self.__red.flashing()
        self.__green.off()
        self.__buzzer.warning_off()

    def is_button_pressed(self):
        return self.__button.button_state()
    
    def reset_button(self):
        self.__button.button_state(False)

class controller:
    def __init__(self, ped_red, ped_green, car_red, car_green, car_amber, button, buzzer, debug):
        self.__traffic_lights = TrafficLightSubsystem(car_red, car_green, car_amber, debug)
        self.__pedestrian_lights = PedestrianSubsystem(ped_red, ped_green, button, buzzer, debug)
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()

    def set_idle(self):
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_lights.show_stop()
        self.__traffic_lights.show_green()
        self.state = "IDLE"

    def set_change_state(self):
        if self.__debug:
            print("State: CHANGING")
        self.__pedestrian_lights.show_stop
        self.__traffic_lights.show_amber
        self.state = "CHANGING"
    
    def set_walk_state(self):
        if self.__debug:
            print("State: WALKING")
        self.__pedestrian_lights.show_walk
        self.__traffic_lights.show_red
        self.state = "WALKING"

    def set_warning_state(self):
        if self.__debug:
            print("State: WARNING")
        self.__pedestrian_lights.show_warning
        self.__traffic_lights.show_red
        self.state = "WARNING"

    def error_state(self):
        if self.__debug:
            print("State: ERROR")
        self.__pedestrian_lights.show_warning
        self.__traffic_lights.show_amber
        self.state = "ERROR"

    def update(self):
        
        print("Running")
        self.last_state_change = time()

        if self.state == "IDLE":
            self.state = self.set_idle
            if time() - self.last_state_change >=10 and self.__pedestrian_lights.is_button_pressed()
                self.state = self.set_change_state
                self.last_state_change = time()
                self.__pedestrian_lights.reset_button

        elif self.state == "CHANGING":
            self.state = self.set_change_state
            if time() - self.last_state_change >= 5:
                self.state = self.set_walk_state
                self.last_state_change = time()

        elif self.state == "WALKING":
            self.state = self.set_walk_state
            if time() - self.last_state_change >=5:
                self.state = self.set_warning_state
                self.last_state_change = time()

        elif self.state == "WARNING":
            self.state = self.set_warning_state
            if time() - self.last_state_change >=5:
                self.state = self.set_idle
                self.last_state_change = time()
