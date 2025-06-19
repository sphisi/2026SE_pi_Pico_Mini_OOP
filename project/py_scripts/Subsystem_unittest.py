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



def Idle()
    print(f"Traffic light is Green /n pedestrian light is red")
    
def changing()
    print(f"Traffic light is amber /n pedestrian light is red")

def walk()
    print(f"Traffic light is red /n pedestrian light is green")

def walk_warning()
    print(f"Traffic light is red /n pedestrian light is flashing")