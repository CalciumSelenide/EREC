#!/usr/bin/env python3
# CalciumSelenide - Wed Nov 12 02:32:55 PM CST 2022
import serial
import serial.tools.list_ports as list_ports
from serialKeyListener import arrowController

if __name__ == "__main__":
    # Try to establish communication with the microbit connected to your laptop serially
    try:
        microBit = serial.Serial(port='/dev/ttyACM0', baudrate='115200', timeout=0.1)
    except Exception as e:
        print("WARNING: " + str(e))
    
    # If there is a microbit that is reachable ...
    if microBit:
        # ... implement the arrowController function
        arrowController(microBit)
    else:
        print("No Micro:Bit was found! :(")
