import cv2
import numpy as np
import constants


global uBGR, dBGR, rBGR, lBGR, fBGR, bBGR

bgr_vals = []
cube_state_string = ""

def getImage(camera):
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
    bgr_values = []
    bgr_array = []
    bgr_values.append(pic[facelet_points[0][0]][facelet_points[0][1]])
    bgr_values.append(pic[facelet_points[1][0]][facelet_points[1][1]])
    bgr_values.append(pic[facelet_points[2][0]][facelet_points[2][1]])
    bgr_values.append(pic[facelet_points[3][0]][facelet_points[3][1]])
    bgr_values.append(pic[facelet_points[4][0]][facelet_points[4][1]])
    bgr_array = np.array(bgr_values)
    return np.mean(bgr_array, axis=0)


def euclidean_distance(color1, color2):
    return np.sqrt(np.sum((color1 - color2) ** 2))


def findClosestCenterFacelet():
    pass


image = getImage(1)
cv2.imshow("image", image)

for facelet in constants.FACELETS:
    bgr_vals.append(getBGR(facelet, image))

uBGR = getBGR(constants.FACELETS[4], image)
rBGR = getBGR(constants.FACELETS[13], image)
fBGR = getBGR(constants.FACELETS[22], image)
dBGR = getBGR(constants.FACELETS[31], image)
lBGR = getBGR(constants.FACELETS[40], image)
bBGR = getBGR(constants.FACELETS[49], image)




while True:
    key = cv2.waitKey(1)

    if key == 27:  # Press ESC key to exit
        break

