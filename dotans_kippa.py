# THIS IS A TESTING FILE FOR SOME VISION STUFF

import cv2
import numpy as np
import constants

global green, yellow, red, blue, white, orange

def euclidean_distance(color1, color2):
    return np.sqrt(np.sum((color1 - color2) ** 2))

def findClosestCenterFacelet(color):
    global green, yellow, red, blue, white, orange

    distances_dict = {euclidean_distance(color, green): "GREEN", euclidean_distance(color, blue): "BLUE",
                      euclidean_distance(color, yellow): "YELLOW", euclidean_distance(color, white): "WHITE",
                      euclidean_distance(color, red) : "RED", euclidean_distance(color, orange) : "ORANGE"}
    distances_list = [euclidean_distance(color, blue), euclidean_distance(color, red), euclidean_distance(color, yellow),
                      euclidean_distance(color, green), euclidean_distance(color, orange), euclidean_distance(color, white)]
    return distances_dict.get(min(distances_list))


def get_state():
    global green, yellow, red, blue, white, orange

    cube_state_string = ""

    # Gets all the center facelet BGR values
    green = [0, 255, 0]
    red = [0, 0, 255]
    yellow = [0, 255, 255]
    blue = [255, 0, 0]
    white = [255, 255, 255]
    orange = [0, 165, 255]

    return findClosestCenterFacelet(np.array([247, 121, 2]))  #Just enter a BGR value in here and it returns its color

print(get_state())

