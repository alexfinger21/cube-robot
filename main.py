import pyfirmata
import tkinter
import customtkinter
import time
import constants
import getCubeState
import kociemba
from StepperMotor import Motor
from Robot import Robot


if __name__ == "__main__":

    # Initialize the Arduino Board
    try:
        board = pyfirmata.Arduino(constants.COM_PORT)
    except:
        print("OOPSY DOOPSY YOU DON't HAVE AN ARDUINO :P")
        exit()

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


# If you want to test turning the robot, simply call the Robot objects "rotate" method
# ↓ ↓ ↓ ↓ Below is some example syntax ↓ ↓ ↓ ↓

# CubeRobot.rotate("R", 2) --> turns the right motor 180 degrees
# CubeRobot.rotate("R'", 1) --> turns the right motor 90 degrees counterclockwise
# CubeRobot.rotate("R", 1) --> turns the right motor 90 degrees clockwise
# CubeRobot.rotate("L", 1) --> turns the left motor 90 degrees clockwise


def solve():
    """
    :return: void function, but it gets the solution for the current state of the cube
    """

    # Gets the cube state
    cube_state = getCubeState.get_state()

    # Inputs the state into kociemba algorithm and gets a solution state6
    solution_string = kociemba.solve(cube_state)
    print(f"solution is --> {solution_string}")
    CubeRobot.solve(solution_string)


def testing():
    # TEST
    print("not kosher")

    CubeRobot.solve("D D2 L' R' R2 L2")
    while True:
        print("clockwise")
        #CubeRobot.rotate("D", 2)  # turns the bottom motor 180 degrees clockwise
        time.sleep(1)
        #CubeRobot.rotate("L", 2)  # turns the left motor 180 degrees clockwise
        time.sleep(1)

        print("counterclockwise")
        #CubeRobot.rotate("D’", 1)  # turns the bottom motor 90 degrees counterclockwise
        time.sleep(1)
        CubeRobot.rotate("L’", 1)  # turns the left motor 90 degrees counterclockwise
        time.sleep(1)
testing()
"""
#Creates the GUI
root_tk = tkinter.Tk()
root_tk.geometry("400x240")
root_tk.title("Cube Robot GUI")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def test():
    testing()

def solveCube():
    print("WARNING: THIS FUNCTION DOESN'T WORK PROPERLY YET!")
    solve()

# Use CTkButton instead of tkinter Button
test_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, text="testing",command=test)
solve_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, text="solve",command=solveCube)

test_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
solve_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

root_tk.mainloop()
*/
"""