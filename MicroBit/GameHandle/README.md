# Yahboom Game Handle
The Yahboom Game Handle is a nifty piece of hardware, but offers no explaination on how to utilize it without thier pre-made .hex file. To mitigate this in the spirit of learning, we have taken the liberty of posting the code for all that wish to use this piece of hardware in a similar manner. 

## 🕹️ gameController.py
This piece of code has the very basics of getting outputs from the controller. Plug the Micro:Bit into a computer, flash the code to your device (**leave the Micro:Bit plugged into the computer**), open a serial reader on the microbit port (usually `/dev/ttyACM0` or `/dev/ttyS0`), and play with the controller.

## 🎮 controllerClass.py
This is a more advanced piece of code in comparison to `gameController.py`: it integrates the lessons learned and establishes a Controller class that initializes all digital pins when created. In additon, it has several on-board functions, the most informational of which are:
  - `buttonBank()`: check the state of all buttons (not including the joystick button) and return them as `[red, green, yellow, blue]`
  - `joyStick()`: check the state of the joystick and its button, then return the values as `[x, y, button]`

## 🗒️ Notes
### Switches, Digital Logic, and Us
When it comes to digital logic and switches, the most common configuration is that a switch, when flipped or pressed, pulls the signal from high to low (taking a digital logic from a `1 ⟶ 0`). 

In both of these codes, you will find: `pinX.set_pull(pinX.PULL_UP)`

This line sets the signal on pinX to default as `HIGH (1)` because we are `pulling pinX up` to a voltage extremely close to the voltage we are providing. When the switch is flipped/pressed, the voltage drops significantly as most of the electrons travel to ground, resulting in `pinX` reading a digital logic value of `LOW (0)`.
