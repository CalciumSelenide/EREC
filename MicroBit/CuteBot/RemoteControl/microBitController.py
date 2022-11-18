#!/usr/bin/env python3
# CalciumSelenide - Sat Nov 12 02:25:59 PM CST 2022
from pynput.keyboard import Key, Listener

serial = None
temp = ""

# These are the keys on our computer that will control our car!
CONTROL_KEYS = [Key.left, Key.right, Key.up, Key.down]

def onPress(key):
    # ON KEY PRESS, we need to identify the key that was pressed
    global serial, CONTROL_KEYS

    # If the key is an arrow key in our CONTROL_KEYS list, then...
    if (key in CONTROL_KEYS):
        # ... print it out, and send it to our Micro:Bit transceiver
        print('{0} pressed'.format(key))
        serial.write(str(key).encode('utf-8'))

def onRelease(key):
    # ON KEY RELEASE, we need to let everyone know no keys are pressed
    global serial, CONTROL_KEYS
    
    # If the key is an arrow key in our CONTROL_KEYS list, then...
    if (key in CONTROL_KEYS):
        # ... print it out, and send it to our Micro:Bit transceiver
        print('{0} release'.format(key))
        serial.write("Key.none".encode('utf-8'))
    
    # If the ESCAPE key was pressed and released, quit the program
    if key == Key.esc:
        # Stop listener
        return False

def arrowController(serialPass):
    # Find what keys are being pressed to control our cars!
    global serial
    serial = serialPass

    # Collect events until released
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()
