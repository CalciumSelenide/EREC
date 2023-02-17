# Remote Control via Laptop and Radio
These three pieces of code work together to form a remote control for the Micro:Bit cars. This allows students to wirelessly control thier cars and change the direction they travel by pressing the arrow keys on one's keyboard. The key presses (and releases) are sent so the car knows what action to perform and when to stop.

## radioTRANSMITTER.py
Flash this piece of code to a Micro:Bit and keep it plugged into your laptop

## serialInterface.py and serialKeyListener.py
The `serialInterface` script uses `serialKeyListener` and listens for the user to push an arrow key. To run it, open a terminal and navigate to the directory with both scripts, then run `python3 serialInterface`. When an arrow key is pressed, the command is sent to the attatched Micro:Bit. The Mirco:Bit then transmits that command to the CuteBot!
