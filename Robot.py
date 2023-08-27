class Robot:

    def __init__(self, down, up, left, right, front, back):
        """
        :param down:
        :param up:
        :param left:
        :param right:
        :param front:
        :param back:
        """

        self.DownMotor = down
        self.UpMotor = up
        self.LeftMotor = left
        self.RightMotor = right
        self.FrontMotor = front
        self.BackMotor = back

    def solve(self, solution_string):
        """
        :param solution_string: string is a string in this format "R U R’ U R U2 R’ U"
                                This is how the kociemba library gives us the solutio
                                link to documentation below, so you know how it all works
                                https://pypi.org/project/kociemba/
        :type solution_string: string
        :return void
        """

        solution_list = solution_string.split()
        for move in solution_list:
            if len(move) == 2:
                if move[1] == "2":
                    self.rotate(move[0], 2)
                    continue
            self.rotate(move, 1)


    def rotate(self, side, turns):
        """
        :param side: The side you want to turn
        :type side: string
        :param turns: Either one or two, one for a 90-degree turn, 2 for 180 degrees
        :type turns: integer
        :return: void function
        """

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
