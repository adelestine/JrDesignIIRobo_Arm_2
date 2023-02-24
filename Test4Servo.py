import pyfirmata
import time
from pyfirmata import Arduino, util
from tkinter import *

board = pyfirmata.Arduino('COM14')


def moveServo(angle):
        board.digital[9].write(angle)


def changeTool(tool):
        if tool == "T1":
                moveServo(45)
        elif tool == "T2":
                moveServo(90)
        elif tool == "T3":
                moveServo(135)
        else:
                #do nothing
                print("")
        return

def main():
        global pin9
        


        iter8 = pyfirmata.util.Iterator(board)
        iter8.start()

        pin9 = board.get_pin('d:9:s')


        # root = Tk()
        # root.title("Servo Control")

        # scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, command=moveServo)
        # scale.pack(anchor=CENTER)

        # root.mainloop()
        while True:
                changeTool("T1")
                time.sleep(1)
                changeTool("T2")
                time.sleep(1)
                changeTool("T3")
                time.sleep(1)

main()




        





# while True:
    
#     board.pinMode(LED_BUILTIN, OUTPUT)
#     board.digitalWrite(LED_BUILTIN, HIGH)
#     board.delay(1000)
#     board.digitalWrite(LED_BUILTIN, LOW)
#     board.delay(1000);
#     # board.digital[13].write(1)
#     # time.sleep(1)
#     # board.digital[13].write(0)
#     # time.sleep(1)