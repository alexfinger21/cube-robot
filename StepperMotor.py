class Motor:
    def __init__(self, dir_pin, step_pin):
        """
        :param dir_pin: This is the digital port for the pin that controls the motor's direction
        :param step_pin: This is the digital port for the pin that controls how fast the motor moves
        """

        self.dirPin = dir_pin
        self.stepPin = step_pin

    def turn(self, degrees):
        """
        :param degrees: the amount of degrees you want your stepper motor to turn
        :return: void function
        """

        iterations = round(degrees / 1.8)
        for i in range(0, iterations):
            self.stepPin.write(1)
            self.stepPin.write(0)

    def setDirection(self, direction):
        """
        :param direction: indicates which direction you want the motor to spin, either clockwise or counterclockwise
        :type: string
        :return:
        """

        if direction == "clockwise":
            self.dirPin.write(0)
        elif direction == "counterclockwise":
            self.dirPin.write(1)
        else:
            print("ERROR: setDirection takes in an argument of 'clockwise' or 'counterclockwise'")
