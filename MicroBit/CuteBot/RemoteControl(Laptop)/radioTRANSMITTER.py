# CalciumSelenide - Wed Feb 14 06:48:15 PM CST 2022
from microbit import *
import radio

class Transciever:
    # Initialize the Controller class
    def __init__(self, messageLength: int, messageQueue: int,
                 radioChannel: int, broadcastStrength: int,
                 messageAddress: int, groupAddress: int):
        # Set all the variables for the controller class to inherit
        self.msgLength = messageLength
        self.msgQueue = messageQueue
        self.msgAddress = messageAddress
        self.grpAddress = groupAddress
        self.radioChannel = radioChannel
        self.broadcastStrength = broadcastStrength

        # Radio status
        self.status = "ON"

        # Radio message parameters
        self.message = ""
        self.rssi = None
        self.timestamp = ""

        # Turn the radio on for the initalization
        radio.on()

        # Set the radio configuration
        radio.config(length=self.msgLength, queue=self.msgQueue,
                     channel=self.radioChannel, power=self.broadcastStrength,
                     address=self.msgAddress, group=self.grpAddress)

        # Setting UART/Serial communications up
        self.serialMessage = ""

    def on(self):
        radio.on()
        self.status = "ON"

# ----------- RADIO functions of the Transciever class --------------
    def off(self):
        radio.off()
        self.status = "OFF"

    def send(self, message):
        radio.send(message)

    def recieve(self):
        tmpDetails = radio.receive_full()
        if tmpDetails:
            self.message, self.rssi, self.timestamp = tmpDetails
        else:
            self.message = ""
            self.rssi = None
            self.timestamp = ""

# ----------- UART/SERIAL functions of the Transciever class --------
    def serialEnable(self, baudRate, msgBits, msgParity, stopBits):
        uart.init(baudrate=baudRate, bits=msgBits, parity=msgParity,
                  stop=stopBits, tx=None, rx=None)

    def serialRead(self):
        serialMsg = uart.readline()
        self.serialMessage = str(serialMsg)

    def serialWrite(self, usrMessage):
        uart.write(usrMessage)

messageLength = 8  # The maximum byte length: can be up to 251 bytes
messageQueue = 1  # The amount of messages that can be stored in queue
radioChannel = 0  # Can be any value between 0 and 83
broadcastStrength = 6  # Can be any value betweeon 0 (weakest) and 7 (strongest)
messageAddress = 0x012345678  # A 32bit address    **
groupAddress = 0  # Can be any value between 0 and 255  **

# ** A messageAddress is like a house, and groupAddress is the person in that
#    that house that the message it to.

# Create your 'myController' object: this is your controller that will
# control your car.
myController = Transciever(messageLength, messageQueue, radioChannel,
                           broadcastStrength, messageAddress, groupAddress)

# Re-initialize UART/Serial to make sure the controller can communicate
# with your laptop over the cord
myController.serialEnable(115200, 8, None, 1)
recievedMessage = ""
temp = None

while True:
    # Check and see if the laptop has sent a command
    myController.serialRead()

    if (myController.serialMessage != "None"):
        # If the laptop has sent a command, format it and grab ALL of it
        recievedMessage += myController.serialMessage[2:-1]
        # display.scroll(recievedMessage)
    else:
        # If there is a final, finished, recieved message, make a decision
        if ((recievedMessage) and (recievedMessage != temp)):
            if (recievedMessage == "Key.left"):
                myController.send("LEFT")
                display.show(Image.ARROW_W)
            if (recievedMessage == "Key.right"):
                myController.send("RIGHT")
                display.show(Image.ARROW_E)
            if (recievedMessage == "Key.up"):
                myController.send("UP")
                display.show(Image.ARROW_N)
            if (recievedMessage == "Key.down"):
                myController.send("DOWN")
                display.show(Image.ARROW_S)

            if (recievedMessage == "Key.none"):
                myController.send("NONE")
                display.show(Image.DIAMOND_SMALL)

            temp = recievedMessage
            recievedMessage = ""
        elif (recievedMessage == temp):
            recievedMessage = ""


    # If the A button is pressed, then broadcast to the reciever, then
    # provide feedback to the laptop.
    if button_a.is_pressed():
        display.show(Image.TARGET)
        myController.send("Hey")
        myController.serialWrite("Sending signal\n")
        sleep(500)
        display.show(Image.DIAMOND_SMALL)
