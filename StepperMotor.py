# import pyfirmata
# import time


class Motor:
    def __init__(self, dir_pin, step_pin):
        # This Motor class takes in the digital port numbers the
        # "direction" and "step" pins are plugged into on the arduino

        self.dirPin = dir_pin
        self.stepPin = step_pin

    def turn(self, degrees):
        # Turns the motor by a given degree value

        iterations = degrees / 1.8
        for i in range(0, iterations):
            self.stepPin.write(1)
            self.stepPin.write(0)

    def setDirection(self, direction):
        # Sets the rotation direction of the motor as either clockwise or counterclockwise

        if direction == "clockwise":
            self.dirPin.write(1)
        if direction == "counterclockwise":
            self.dirPin.write(0)
        else:
            print("ERROR: setDirection takes in an argument of 'clockwise' or 'counterclockwise'")