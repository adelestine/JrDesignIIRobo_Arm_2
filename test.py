import pyfirmata
import time
from pyfirmata import Arduino, util
board = pyfirmata.Arduino('COM5')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(4)




# while True:
    
#     board.pinMode(LED_BUILTIN, OUTPUT)
#     board.digitalWrite(LED_BUILTIN, HIGH)
#     board.delay(1000)
#     board.digitalWrite(LED_BUILTIN, LOW)
#     board.delay(1000);
#     # board.digital[13].write(1)
#     # time.sleep(1)
#     # board.digital[13].write(0)
#     # time.sleep(1)p