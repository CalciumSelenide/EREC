# CalciumSelenide - Wed Feb 14 06:48:15 PM CST 2022
from microbit import *
import music
from machine import time_pulse_us

# -- BUILD THE I2C DRIVERS ---------------
I2CAddr = 16

# MOTOR VALUES
leftMotor = 1
rightMotor = 2
fullSpeed = 85
maxSpeed = 100
minSpeed = -100
forwardMotor = 2
backwardMotor = 1

# HEADLIGHT VALUES
leftLED = 4
rightLED = 8
minLED = 0
maxLED = 255
minLight = 5

# ULTRASONIC VALUES
trigger = pin8
echo = pin12
trigger.write_digital(0)
echo.read_digital()

# -- LED I2C DRIVERS ---------------------
def ledHelper(LED: int, red: int = minLED, green: int = minLED, blue: int = minLED):
    buffer = bytearray(4)

    # Which LED are we setting? Left or Right?
    buffer[0] = LED

    # Check for extreme values. If they are too small or too large, fix them
    buffer[1] = red if minLED <= red <= maxLED else minLED
    buffer[2] = green if minLED <= green <= maxLED else minLED
    buffer[3] = blue if minLED <= blue <= maxLED else minLED

    # Tell CuteBot to change the LED color!
    i2c.write(I2CAddr, buffer)

def setLeftLED(red: int = 0, green: int = 0, blue: int = 0):
    # Turn on the Left LED!
    ledHelper(leftLED, red, green, blue)

def setRightLED(red: int = 0, green: int = 0, blue: int = 0):
    # Turn on the Right LED!
    ledHelper(rightLED, red, green, blue)

def headLightsOn():
    # There's no telling where they're going...switch on the lights!
    setLeftLED(maxLED, maxLED, maxLED)
    setRightLED(maxLED, maxLED, maxLED)

def headLightsOff():
    # The sun's out...stop wasting electricity!
    setLeftLED(minLED, minLED, minLED)
    setRightLED(minLED, minLED, minLED)

def speedHelper(motorPosition: int, speed: int):
    buffer = bytearray(4)
    buffer[0] = motorPosition

    # Test for extreeme cases, then correct as needed
    if speed > maxSpeed:
        speed = maxSpeed
    elif speed < minSpeed:
        speed = minSpeed

    # Set buffer values to write
    if speed >= 0:
        buffer[1] = forwardMotor
    else:
        speed = speed * -1
        buffer[1] = backwardMotor

    buffer[2] = speed
    buffer[3] = 0

    i2c.write(I2CAddr, buffer)

def setSpeed(leftSpeed: int, rightSpeed: int):
    # Set the speed for the left motor using the I2C address and desired value
    speedHelper(leftMotor, leftSpeed)

    # Set the speed for the left motor using the I2C address and desired value
    speedHelper(rightMotor, rightSpeed)

def goForward(leMotor: int = fullSpeed, riMotor: int = fullSpeed):
    # CAR GOES VROOM!
    setSpeed(leMotor, riMotor)

def goBackward(leMotor: int = fullSpeed, riMotor: int = fullSpeed):
    # Beep...Beep...Beep...
    setSpeed(-leMotor, -riMotor)

def stop():
    # HALT
    setSpeed(0, 0)

def turnLeft(leMotor: int = -fullSpeed, riMotor: int = fullSpeed):
    # dnuor' thgir em nips uoY
    setSpeed(leMotor, riMotor)

def turnRight(leMotor: int = fullSpeed, riMotor: int = -fullSpeed):
    # You spin me right 'round
    setSpeed(leMotor, riMotor)

def ultrasonicDistance(trigger, echo):
    # This function returns the range to find the
    # distance between the car and the object

    # Trigger burst
    trigger.write_digital(1)
    trigger.write_digital(0)

    # Try to catch the echo back, then convert to seconds
    microSeconds = time_pulse_us(echo, 1)
    echoTime = microSeconds / 1000000

    # Calculate distance in centimeters, then display
    distanceCM = (echoTime / 2) * 34300
    return int(distanceCM)

def ultrasonicSense(trigger, echo):
    distance = ultrasonicDistance(trigger, echo)

    if (distance <= 30):
        # Back up to access the situation.
        stop()
        setLeftLED(255, 0, 0)
        setRightLED(255, 0, 0)
        sleep(200)
        goBackward(50, 50)
        sleep(500)

        # Check left
        turnLeft(0, 45)
        sleep(400)
        stop()
        leDistance = ultrasonicDistance(trigger, echo)
        turnLeft(0, -45)
        sleep(400)

        # Check right
        turnRight(45, 0)
        sleep(400)
        stop()
        riDistance = ultrasonicDistance(trigger, echo)
        turnRight(-45, 0)
        sleep(400)

        # Compare the distances: find which one is BIGGER
        if (leDistance >= riDistance):
            turnLeft(0, 45)
            sleep(400)
            goForward()
        else:
            turnRight(45, 0)
            sleep(400)
            goForward()
    else:
        goForward()

# -- E.O.I2C DRIVERS ---------------
def setState(direction: str = ""):
    # This function sets the car's state.
    # - Forward
    # - Backward
    # - Turning (left or right)
    # - Stopped
    if not direction:
        display.show(Image.TARGET)
        sleep(1500)
    else:
        direction = str(direction, 'UTF-8')

    a_count = 0
    b_count = 0
    state = ""

    a_count = button_a.get_presses() - 1
    b_count = button_b.get_presses() - 1

    if ((a_count == 1) or (direction == "UP")):
        # Go forward
        for speed in range(100):
            setSpeed(speed, speed)
        state = "A1"
    elif ((a_count == 2) or (direction == "DOWN")):
        # Go backward
        goBackward()
        state = "A2"
    elif ((a_count == 3) or (direction == "NONE")):
        # Halt
        stop()
        state = "A3"
    elif ((b_count == 1) or (direction == "LEFT")):
        # Turn left
        turnLeft()
        state = "B1"
    elif ((b_count == 2) or (direction == "RIGHT")):
        # Turn right
        turnRight()
        state = "B2"
    elif b_count == 3:
        # Ultrasonic detection mode - ENGAGE
        state = "B3"
        stop()
        music.play(music.POWER_UP)
    else:
        state = "00"

    display.clear()
    return state

def checkState(state):
    # This function checks the car's state and applys the correct
    # LED animation. (Turning with blinkers, blinking reverse, brake lights)
    if state == "A1":
        pass
    elif state == "A2":
        # Beep...beep...beep...
        setLeftLED(255, 0, 0)
        setRightLED(255, 0, 0)
        sleep(400)
        setLeftLED(0, 0, 0)
        setRightLED(0, 0, 0)
        sleep(400)
    elif state == "A3":
        # HALT!
        setLeftLED(255, 0, 0)
        setRightLED(255, 0, 0)
        sleep(1000)
    elif state == "B1":
        # Blinker! We have to indicate we are turning!
        setLeftLED(255, 247, 0)
        sleep(400)
        setLeftLED(0, 0, 0)
        sleep(400)
    elif state == "B2":
        # Blinker! We have to indicate we are turning!
        setRightLED(255, 247, 0)
        sleep(400)
        setRightLED(0, 0, 0)
        sleep(400)
    elif state == "B3":
        # Detect with Ultrasonic!
        ultrasonicSense(trigger, echo)
    else:
        pass
# -- END OF DEVICE DEFINITIONS -------
