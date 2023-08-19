# All the digital pins for the motors
BOTTOM_MOTOR_STEP_PIN = 2
BOTTOM_MOTOR_DIR_PIN = 8

LEFT_MOTOR_STEP_PIN = 3
LEFT_MOTOR_DIR_PIN = 9

BACK_MOTOR_STEP_PIN = 3
BACK_MOTOR_DIR_PIN = 9

RIGHT_MOTOR_STEP_PIN = 4
RIGHT_MOTOR_DIR_PIN = 10

TOP_MOTOR_STEP_PIN = 3
TOP_MOTOR_DIR_PIN = 9

FRONT_MOTOR_STEP_PIN = 3
FRONT_MOTOR_DIR_PIN = 9

# All the fixed pixel (x, y) locations of each facelet location
# We have 5 locations per facelet in order to average HSV values to minimize distraction in the image
FACELETS_CAM_1 = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # U9

                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # R9

                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # F8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]  # F9

FACELETS_CAM_2 = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # D9

                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # L9

                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B1
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B2
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B3
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B4
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B5
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B6
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B7
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B8
                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],  # B9
            ]

