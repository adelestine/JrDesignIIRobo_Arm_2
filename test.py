import pyfirmata
import time
import streams
from pyfirmata import Arduino, util
from servo import servo
board = pyfirmata.Arduino('COM12')
myServo = servo.Servo(board, 9)
dir = 1
while True:
        myServo.write(45)
        time.sleep(1)
        myServo.write(90)
        time.sleep(1)
        myServo.write(135)
        time.sleep(1)
        print(0)



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