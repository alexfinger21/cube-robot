import cv2

# This is all just some goofy stuff to get pixel values for da vision for da rubiks cube
global print_list
print_list = []


def mouse_click(event, x, y, flags, param):
    global print_list
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at pixel location on snapshot: ({x}, {y})")
        print_list.append((x, y))

        if len(print_list) == 5:

            print(print_list)
            print_list.clear()


cap = cv2.VideoCapture(0)  # REPLACE "cap" VARIABLE WITH IMAGE RETRIEVED FROM CAMERA
ret, frame = cap.read()
cv2.imshow("Snapshot", frame)
cv2.setMouseCallback("Snapshot", mouse_click)
while True:

    key = cv2.waitKey(1)

    if key == 27:  # Press ESC key to exit
        break

cap.release()
print("H")
