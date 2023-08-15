import pyfirmata
import time

board = pyfirmata.Arduino("COM3")
print("Communication Started!!!")

print("not kosher")

while True:
    print("here")
    for i in range(int(360/1.8)):
        board.digital[2].write(1)
        board.digital[3].write(1)
        board.digital[4].write(1)

        time.sleep(0.001)
        board.digital[2].write(0)
        board.digital[3].write(0)
        board.digital[4].write(0)

    time.sleep(1)