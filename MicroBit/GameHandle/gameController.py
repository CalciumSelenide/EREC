# CalciumSelenide - Thurs Nov 17 11:47:31 PM CST 2022
# YahBoom GameHandle Controller Code
from microbit import *

# Enable the controller buttons
pin8.set_pull(pin8.PULL_UP)    # JoyButton
pin13.set_pull(pin13.PULL_UP)  # RED
pin14.set_pull(pin14.PULL_UP)  # GREEN
pin15.set_pull(pin15.PULL_UP)  # BLUE
pin16.set_pull(pin16.PULL_UP)  # YELLOW

while True:
    # JoyStick values for the Game Controller
    joyY = str(pin1.read_analog())
    joyX = str(pin2.read_analog())
    joyButton = pin8.read_digital()

    # Button bank
    red = pin13.read_digital()
    green = pin14.read_digital()
    blue = pin15.read_digital()
    yellow = pin16.read_digital()

    print("X: %04d, Y: %04d , BTN: %s| RED: %s, YEL: %s, GRE: %s, BLU: %s" %
          (int(joyX), int(joyY), str(joyButton), str(red), str(yellow),
           str(green), str(blue)))
