# CalciumSelenide - Wed Feb 14 06:48:15 PM CST 2022
from microbit import *
import cutebotcar as car
import radioRECIEVER as transciever

state = "00"
car.headLightsOff()
display.show(Image.HAPPY)
while True:
    # Automatic Headlights!
    light = display.read_light_level()
    if light < car.minLight:
        car.headLightsOn()
    else:
        car.headLightsOff()

    transciever.myBot.recieve()

    if transciever.myBot.message:
        state = car.setState(transciever.myBot.message[3:])
        #display.show(state)

    # If both a and b are pressed, we want to change the state of our car
    # if button_a.is_pressed() and button_b.is_pressed():
    #    state = car.setState()
    #    display.show(state)
    #    sleep(500)
    #    display.show(Image.HAPPY)
    # else:
    #    car.checkState(state)

    #    # If we brake, we want to turn off the brake lights after 1 second
    #    if state == "A3":
    #        state = "00"
