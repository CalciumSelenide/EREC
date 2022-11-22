# Yahboom Game Handle
The Yahboom Game Handle is a nifty piece of hardware, but offers no explaination on how to utilize it without thier pre-made .hex file. To mitigate this in the spirit of learning, we have taken the liberty of posting the code for all that wish to use this piece of hardware in the manner that we do. 

## 🕹️ gameController.py
This piece of code has the very basics of getting outputs from the controller. Plug the microbit into a computer, flash the code to your device (**leave the microbit plugged into the computer**), open a serial reader on the microbit port (usually `/dev/ttyACM0` or `/dev/ttyS0`), and play with the controller.

## 🎮 controllerClass.py
Stay tuned...

## 🗒️ Notes
### Switches, Digital Logic, and Us
When it comes to digital logic with switches, the industry standard is that a switch, when flipped or pressed, pulls the signal from high to low (taking a digital logic from a `1 ⟶ 0`). 

In both of these codes, you will find: `pinX.set_pull(pinX.PULL_UP)`

This line sets the signal on pinX to default as `HIGH (1)` because we are `pulling pinX up` to a voltage extremely close to the voltage we are providing. When the switch is flipped/pressed, the voltage drops significantly as most of the electrons travel to ground, resulting in that pin giving a digital logic value of `LOW (0)`.
