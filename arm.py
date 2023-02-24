import math
import pyfirmata
import time
from pyfirmata import Arduino, util
board = pyfirmata.Arduino('COM5')

def welcome():
    file = input('What file would you like to run?:    ')
    return file

#Used to parse and seperate the G code file into correst peicess
def parse_file(file):
    #filename = input("What file would you like to run?:  ")
    #file_object = open(filename, "r")
    file_object = open(file, "r")
    i = 0
    m72check = 0
    for curr_line in file_object:
        curr_line = curr_line.replace(" ","")
        curr_line = curr_line.replace("\n","")
        if "M2" in curr_line:
            break
        if "M72" in curr_line:
            m72check = 1
            continue
        if "M6" in curr_line:
            coord_dict['Y'].append(coord_dict['Y'][i-1])            
            coord_dict['X'].append(coord_dict['X'][i-1])
            coord_dict['G'].append(curr_line)
            coord_dict['F'].append(coord_dict['F'][i-1])
            i = i+1
            continue
            
        x_loc = curr_line.find("X")
        y_loc = curr_line.find("Y")
        g_loc = curr_line.find("G")
        if "G01" in curr_line:
            f_loc = curr_line.find("F")
            coord_dict['Y'].append(curr_line[y_loc+1:f_loc])            
            coord_dict['X'].append(curr_line[x_loc+1:y_loc])
            coord_dict['G'].append(curr_line[:x_loc])
            coord_dict['F'].append(curr_line[f_loc+1:])
        else:
            coord_dict['Y'].append(curr_line[y_loc+1:])            
            coord_dict['X'].append(curr_line[x_loc+1:y_loc])
            coord_dict['G'].append(curr_line[:x_loc])
            coord_dict['F'].append(coord_dict['F'][i-1])
        if m72check == 1:
            coord_dict['F'][i] = 1000
        i = i+1
        
        

    #print(coord_dict)

#Uses inverse kinematics to determine the desired angle based on coordinates
def angle(x, y, scale):
    L = 5.25
    if(scale == 'mm'):
        L = 5.25 * 25.4     
    
    hypotnuse = math.sqrt(pow(x,2) + pow(y,2))
    s1 = hypotnuse/2
    s2 = math.sqrt(pow(L,2) - pow(s1,2))

    aB = math.atan(s2/s1)
    x2 = x/2
    y2 = y/2

    aA = math.atan(x2/y2)

    servo1angle = aA+aB
    servo1angle = (servo1angle/ (2* 3.141)) * 360

    x3 = -L*math.sin(aA+aB)
    y3 = -L*math.cos(aA+aB)
    servo2angle= math.atan((x-x3)/(y-y3));  

    servo2angle= (servo2angle / (2 * 3.14159)) * 360

    if ((y-y3)>0):
        servo2angle=servo2angle-180
    angles = [servo1angle, servo2angle]
    return angles

#Runs motors like normal, changes based on g commands
def run_servos_G00(n1, n2, c1, c2, scale, line):
    angles = angle(n1, n2, scale)
    servo1angle = angles[0]
    servo2angle = angles[1]
    servo.append(servo1angle)
    servo2.append(servo2angle)
    #Determines how far to travel based on new desired angle and previous angle 
    movementservo1 = servo[len(servo)-1] - servo[len(servo)-2]
    movementservo2 = servo[len(servo2)-1] - servo[len(servo2)-2]
    #Moves servo1 backwards IE negative angle
    num1steps = movementservo1/1.8
    num2steps = movementservo2/1.8
    if(movementservo1 < 0):
        for i in range(0-int(num1steps)):
            board.digital[5].write(0)
            board.digital[2].write(1)
            board.digital[2].write(0)
            #time.sleep(1/(int(coord_dict['F'][line])))
            time.sleep(0.01)
    #Servo angle is positive
    else:
        for i in range(int(num1steps)):
            board.digital[5].write(1)
            board.digital[2].write(1)
            board.digital[2].write(0)
            #time.sleep(1/(int(coord_dict['F'][line])))
            time.sleep(0.01)
    #Moves servo2 backwards IE negative angle
    #print(servo2)
    if(num2steps < 0):
        for i in range(0-int(num2steps)):
            board.digital[6].write(1)
            board.digital[3].write(1)
            board.digital[3].write(0)
            #time.sleep(1/(int(coord_dict['F'][line])))
            time.sleep(0.01)
    #Servo2 angle is positive
    else:        
        for i in range(int(num2steps)):
            board.digital[6].write(0)
            board.digital[3].write(1)
            board.digital[3].write(0)
            #time.sleep(1/(int(coord_dict['F'][line])))
            time.sleep(0.01)

#Once the G code file is parsed, we use this to run the entire program
def run_program():
    for i in range(len(coord_dict['X'])):
        #print(int(coord_dict['X'][i]), int(coord_dict['Y'][i]))
            if coord_dict['G'][i] == 'G00':
                run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'inches', i)
            elif coord_dict['G'][i] == 'G01':
                run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'inches', i)
            elif coord_dict['G'][i] == 'G90':
                run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'inches', i)
            elif coord_dict['G'][i] == 'G91':
                n1 = int(coord_dict['X'][i]) + int(coord_dict['X'][i-1])
                n2 = int(coord_dict['Y'][i]) + int(coord_dict['Y'][i-1])
                run_servos_G00(n1, n2, int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'inches' , i)
            elif coord_dict['G'][i] == 'G20':
                run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'inches', i)
            elif coord_dict['G'][i] == 'G21':
                run_servos_G00(int(coord_dict['X'][i])/25.4, int(coord_dict['Y'][i])/25.4, int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]), 'mm', i)
            elif coord_dict['G'][i] == 'M6':
                 print()

servo = []
servo2 = []

coord_dict = {"X":[], "Y":[], "G":[], "F":[]}
file = welcome()
parse_file(file)
time.sleep(2)
print('go')
run_program()
print(coord_dict)   
print(servo)
print(servo2)
    
    

