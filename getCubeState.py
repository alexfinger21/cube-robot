import cv2
import numpy as np
import constants

global uBGR, dBGR, rBGR, lBGR, fBGR, bBGR


def getImage(camera):
    # Gets the camera image, we have two so this is essential

    if camera == 1:
        ret, frame = cv2.VideoCapture(0).read()  # REPLACE WITH THE ACTUAL IMAGE FROM CAMERA 1
    elif camera == 2:
        ret, frame = cv2.VideoCapture(0).read()  # REPLACE WITH THE ACTUAL IMAGE FROM CAMERA 2
    else:
        print("Your a stinki poo")
        frame = "goofy"
        exit()
    return frame


def getBGR(facelet_points, pic):
    # Averages the 5 BGR values and returns a single value

    bgr_values = []
    bgr_values.append(pic[facelet_points[0][0]][facelet_points[0][1]])
    bgr_values.append(pic[facelet_points[1][0]][facelet_points[1][1]])
    bgr_values.append(pic[facelet_points[2][0]][facelet_points[2][1]])
    bgr_values.append(pic[facelet_points[3][0]][facelet_points[3][1]])
    bgr_values.append(pic[facelet_points[4][0]][facelet_points[4][1]])
    bgr_array = np.array(bgr_values)
    average = np.mean(bgr_array, axis=0)
    return average.astype(int)


def euclidean_distance(color1, color2):
    return np.sqrt(np.sum((color1 - color2) ** 2))


def findClosestCenterFacelet(color):
    global uBGR, rBGR, fBGR, lBGR, dBGR, bBGR

    distances_dict = {euclidean_distance(color, uBGR): "U", euclidean_distance(color, rBGR): "R",
                      euclidean_distance(color, fBGR): "F", euclidean_distance(color, dBGR): "D",
                      euclidean_distance(color, lBGR) : "L", euclidean_distance(color, bBGR) : "B"}
    distances_list = [euclidean_distance(color, uBGR), euclidean_distance(color, rBGR), euclidean_distance(color, fBGR),
                      euclidean_distance(color, dBGR), euclidean_distance(color, lBGR), euclidean_distance(color, bBGR)]
    return distances_dict.get(min(distances_list))


def get_state():
    global uBGR, dBGR, lBGR, rBGR, fBGR, bBGR

    bgr_vals = []
    cube_state_string = ""

    imageCam1 = getImage(1)
    imageCam2 = getImage(2)

    # cv2.imshow("image", imageCam1)

    for facelet in constants.FACELETS_CAM_1:
        bgr_vals.append(getBGR(facelet, imageCam1))

    for facelet in constants.FACELETS_CAM_2:
        bgr_vals.append(getBGR(facelet, imageCam2))

    # Gets all the center facelet BGR values
    uBGR = getBGR(constants.FACELETS_CAM_1[4], imageCam1)
    rBGR = getBGR(constants.FACELETS_CAM_1[13], imageCam1)
    fBGR = getBGR(constants.FACELETS_CAM_1[22], imageCam1)
    dBGR = getBGR(constants.FACELETS_CAM_2[4], imageCam2)
    lBGR = getBGR(constants.FACELETS_CAM_2[13], imageCam2)
    bBGR = getBGR(constants.FACELETS_CAM_2[22], imageCam2)

    bgr_vals = np.array(bgr_vals)

    for val in bgr_vals:
        cube_state_string += findClosestCenterFacelet(val)

    # If cube_state_string.count("U") != 9 or cube_state_string.count("D") != 9 or cube_state_string.count("R") != 9 or
    # cube_state_string.count("L") != 9 or cube_state_string.count("F") != 9 or cube_state_string.count("B") != 9:
    # Print(f"Get cube state failed! String retrieved {cube_state_string}")
    # exit()

    return cube_state_string

#print(get_state())
