from pedestrian_button import Pedestrian_Button

red_ped_LED = Pedestrian_Button(7, False)
green_ped_LED = Pedestrian_Button(8, False)

if pedestrian_waiting == False:
    print("red light is in {red_ped_LED.__pin}\n green light is in {green_ped_LED.__pin}")
elif pedestrian_waiting == True:
    