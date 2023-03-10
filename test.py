import pyfirmata
import time
from pyfirmata import Arduino, util
board = pyfirmata.Arduino('COM6')

board.digital[7].write(0)
dir = 1
time.sleep(2)
print('gp')
j = 0
for i in range(1000000):
        # board.digital[2].write(1)
        # board.digital[2].write(0)
        # time.sleep(.001)
        
        # board.digital[3].write(1)
        # board.digital[3].write(0)
        # time.sleep(.001)
        
        board.digital[4].write(1)
        board.digital[4].write(0)
        time.sleep(.001)
        print(i)        

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