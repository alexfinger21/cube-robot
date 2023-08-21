import pyfirmata
import time
import constants
import getCubeState
from StepperMotor import Motor
from Robot import Robot

# Initialize the Arduino Board
board = pyfirmata.Arduino("COM3")
print("Communication Started!!!")


# YOU NEED TO CHANGE THE PORT NUMBERS IN CONSTANTS.PY!!!
# Initializes all the Motors
DownMotor = Motor(board.digital[constants.BOTTOM_MOTOR_DIR_PIN], board.digital[constants.BOTTOM_MOTOR_STEP_PIN])
UpMotor = Motor(board.digital[constants.TOP_MOTOR_DIR_PIN], board.digital[constants.TOP_MOTOR_STEP_PIN])
LeftMotor = Motor(board.digital[constants.LEFT_MOTOR_DIR_PIN], board.digital[constants.LEFT_MOTOR_STEP_PIN])
RightMotor = Motor(board.digital[constants.RIGHT_MOTOR_DIR_PIN], board.digital[constants.RIGHT_MOTOR_STEP_PIN])
FrontMotor = Motor(board.digital[constants.FRONT_MOTOR_DIR_PIN], board.digital[constants.FRONT_MOTOR_STEP_PIN])
BackMotor = Motor(board.digital[constants.BACK_MOTOR_DIR_PIN], board.digital[constants.BACK_MOTOR_STEP_PIN])

# Initializes the Robot
CubeRobot = Robot(DownMotor, UpMotor, LeftMotor, RightMotor, FrontMotor, BackMotor)

# The only thing left to program is using the kociemba library to feed a solution string into the CubeRobot
# I would suggest installing kociemba on your laptop if you have not already, it is not an easy process like
# most python libraries, you will need up+dated C++ build tools and took me a while to figure out. Alex and I have
# it installed on our PC's but let's all get it installed on our laptops.

# If you want to test turning the robot, simply call the Robot objects "rotate" method
# ↓ ↓ ↓ ↓ Below is some example syntax ↓ ↓ ↓ ↓

# CubeRobot.rotate("R", 2) --> turns the right motor 180 degrees
# CubeRobot.rotate("R'", 1) --> turns the right motor 90 degrees counterclockwise
# CubeRobot.rotate("R", 1) --> turns the right motor 90 degrees clockwise
# CubeRobot.rotate("L", 1) --> turns the left motor 90 degrees clockwise


def solve():
    cube_state = getCubeState.get_state()
    print(cube_state)


def testing():
    # TEST
    print("not kosher")

    CubeRobot.solve("D D2 L' R' R2 L2")
    while True:
        print("clockwise")
        CubeRobot.rotate("D", 2)  # turns the bottom motor 180 degrees clockwise
        time.sleep(1)
        CubeRobot.rotate("L", 2)  # turns the left motor 180 degrees clockwise
        time.sleep(1)
        CubeRobot.rotate("R", 2)  # turns the right motor 180 degrees clockwise
        time.sleep(1)

        print("counterclockwise")
        CubeRobot.rotate("D’", 1)  # turns the bottom motor 90 degrees counterclockwise
        time.sleep(1)
        CubeRobot.rotate("L’", 1)  # turns the left motor 90 degrees counterclockwise
        time.sleep(1)
        CubeRobot.rotate("R’", 1)  # turns the right motor 90 degrees counterclockwise
        time.sleep(1)


testing()
