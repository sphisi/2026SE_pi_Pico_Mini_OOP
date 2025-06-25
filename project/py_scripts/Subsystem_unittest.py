from controller import TrafficLightSubsystem, PedestrianSubsystem
from led_light import led_light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

#pedestrian light instantitation
led_ped_red = led_light(19, True, True)
led_ped_green = led_light(17, False, True)
#car light instantiation
red_car_led = led_light(3, False, True)
amber_car_led = led_light(5, False, True)
green_car_led = led_light(6, False, True)
#other instnatiation
button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)
#traffic light instantiation 
traffic_subsystem = TrafficLightSubsystem(red_car_led, amber_car_led, green_car_led, debug=False)
pedestrian_subsystem = PedestrianSubsystem(led_ped_green, led_ped_red, button, buzzer, debug=False)


def traffic_subsystem_driver():
    print("beggining traffic light susbystem test")
    #test red light
    print("red light on for 3 sec")
    traffic_subsystem.show_red()
    sleep(3)
    #test amber light
    print("amber light on for 3 sec")
    traffic_subsystem.show_amber()
    sleep(3)
    #test green light
    print("green light on for 3 sec")
    traffic_subsystem.show_green()
    sleep(3)   
    print("ending traffic light subsystem test")

def pedestrian_subsystem_driver():
    #test stop
    print("testing stop: red light on, buzzer off. for 3 sec")
    pedestrian_subsystem.show_stop()
    sleep(3)
    #test walk
    print("testing walk: green light on, buzzer on. for 3 sec")
    pedestrian_subsystem.show_walk()
    sleep(3)
    #test warning
    print("testing warning: red light flashing, buzzer off. for 3 sec")
    pedestrian_subsystem.show_warning()
    sleep(3)
    print("ending pedestrian button test")
    




def Idle()
    print(f"Traffic light is Green /n pedestrian light is red")
    
def changing()
    print(f"Traffic light is amber /n pedestrian light is red")

def walk()
    print(f"Traffic light is red /n pedestrian light is green")

def walk_warning()
    print(f"Traffic light is red /n pedestrian light is flashing")


