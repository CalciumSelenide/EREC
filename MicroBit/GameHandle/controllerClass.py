# CalciumSelenide - Wed Nov 23 11:21:09 PM CST 2022
# YahBoom GameHandle Controller Class Code
from microbit import *

class Controller:
    def __init__(self):
        # Enable the controller buttons
        pin8.set_pull(pin8.PULL_UP)    # JoyButton
        pin13.set_pull(pin13.PULL_UP)  # RED
        pin14.set_pull(pin14.PULL_UP)  # GREEN
        pin15.set_pull(pin15.PULL_UP)  # BLUE
        pin16.set_pull(pin16.PULL_UP)  # YELLOW

    def joyStickX(self):
        # Read the 'X' value of the joystick
        x = pin2.read_analog()
        return x

    def joyStickY(self):
        # Read the 'Y' value of the joystick
        y = pin1.read_analog()
        return y

    def joyStickButton(self):
        # See if the joystick has been pressed
        btn = pin8.read_digital()

        if not btn:
            # If the button is pressed (0) return True!
            return True
        else:
            # If the button is not pressed (1) return False!
            return False

    def redButtonPressed(self):
        # See if the red button has been pressed
        red = pin13.read_digital()

        if not red:
            # If the button is pressed (0) return True!
            return True
        else:
            # If the button is not pressed (1) return False!
            return False

    def greenButtonPressed(self):
        # See if the green button has been pressed
        green = pin14.read_digital()

        if not green:
            # If the button is pressed (0) return True!
            return True
        else:
            # If the button is not pressed (1) return False!
            return False

    def yellowButtonPressed(self):
        # See if the yellow button has been pressed
        yellow = pin16.read_digital()

        if not yellow:
            # If the button is pressed (0) return True!
            return True
        else:
            # If the button is not pressed (1) return False!
            return False

    def blueButtonPressed(self):
        # See if the blue button has been pressed
        blue = pin15.read_digital()

        if not blue:
            # If the button is pressed (0) return True!
            return True
        else:
            # If the button is not pressed (1) return False!
            return False

    def buttonBank(self):
        # Check the state of ALL the buttons (excluding the joystick)
        red = self.redButtonPressed()
        green = self.greenButtonPressed()
        yellow = self.yellowButtonPressed()
        blue = self.blueButtonPressed()

        # Return list of button states
        return [red, green, yellow, blue]

    def joyStick(self):
        # Check the state of the joy stick
        x = self.joyStickX()
        y = self.joyStickY()
        btn = self.joyStickButton()

        # Return list of joystick attributes
        return [x, y, btn]

    def joyStickInterpret(self):
        # X: LEFT = 1023, RIGHT = 0, MIDDLE = 490-510
        # Y: TOP = 0, BOTTOM = 1023, MIDDLE = 490-510
        x, y, btn = self.joyStick()
        
        # Center Values for when the  joystick is at rest
        x0Right = 490
        y0Top = 490
        x0Left = 510
        y0Bottom = 510
        
        # If the joystick is moved either left or right, return the percentage
        # of the distance from the center/origin
        if (x > x0Left):
            xMagnitude = int(float((x - x0Left)/x0Left) * 100)
        elif (x < x0Right):
            xMagnitude = int(float((x - x0Right)/x0Right) * -100)
        else:
            xMagnitude = 0
        
        # If the joystick is moved either up or down, return the percentage
        # of the distance from the center/origin
        if (y > y0Bottom):
            yMagnitude = int(float((y - y0Bottom)/y0Bottom) * 100)
        elif (y < y0Top):
            yMagnitude = int(float((y - y0Top)/y0Top) * -100)
        else:
            yMagnitude = 0

        return [xMagnitude, yMagnitude]

########### END OF CLASS DEFINITION ################
myController = Controller()
while True:
    joyInfo1 = myController.joyStick()
    joyInfo2 = myController.buttonBank()
    print("X: %04d, Y: %04d, BTN: %s | RED: %s, GRE: %s, YEL: %s, BLU:%s" %
          (joyInfo1[0], joyInfo1[1], joyInfo1[2], joyInfo2[0], joyInfo2[1], 
           joyInfo2[2], joyInfo2[3]))
