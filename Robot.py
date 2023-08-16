# import pyfirmata
# import constants
# from StepperMotor import Motor


class Robot:

    def __init__(self, down, up, left, right, front, back):
        # This Robot class takes in 6 Motor objects as parameters

        self.DownMotor = down
        self.UpMotor = up
        self.LeftMotor = left
        self.RightMotor = right
        self.FrontMotor = front
        self.BackMotor = back

    def solve(self, solution_string):
        # Solution string is a string in this format "R U R’ U R U2 R’ U"
        # This is how the kociemba library gives us the solution
        # link to documentation below, so you know how it all works
        # https://pypi.org/project/kociemba/

        solution_list = solution_string.split()
        for move in solution_list:
            if len(move) == 2:
                if move[1] == "2":
                    self.rotate(move[0], 2)
                    continue
            self.rotate(move, 1)

    def rotate(self, side, turns):
        # turns is an integer either 1 or 2
        # this rotates the stepper motor either 180 or 90 degrees counterclockwise or clockwise
        # on whichever motor you specify.

        if (turns != 1) and (turns != 2):
            print("ERROR: turns has to be an integer either 1 or 2 (1 for 90 degree turn 2 for a 180 degree turn)")
        if side == "R":
            self.RightMotor.setDirection("clockwise")
            self.RightMotor.turn(90 * turns)
        elif side == "R’":
            self.RightMotor.setDirection("counterclockwise")
            self.RightMotor.turn(90 * turns)
        elif side == "L":
            self.LeftMotor.setDirection("clockwise")
            self.LeftMotor.turn(90 * turns)
        elif side == "L’":
            self.LeftMotor.setDirection("counterclockwise")
            self.LeftMotor.turn(90 * turns)
        elif side == "U":
            self.UpMotor.setDirection("clockwise")
            self.UpMotor.turn(90 * turns)
        elif side == "U’":
            self.UpMotor.setDirection("counterclockwise")
            self.UpMotor.turn(90 * turns)
        elif side == "D":
            self.DownMotor.setDirection("clockwise")
            self.DownMotor.turn(90 * turns)
        elif side == "D’":
            self.DownMotor.setDirection("counterclockwise")
            self.DownMotor.turn(90 * turns)
        elif side == "F":
            self.FrontMotor.setDirection("clockwise")
            self.FrontMotor.turn(90 * turns)
        elif side == "F’":
            self.FrontMotor.setDirection("counterclockwise")
            self.FrontMotor.turn(90 * turns)
