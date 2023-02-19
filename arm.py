import math

servo = []
servo2 = []
#Runs motors like normal
def run_servos_G00(n1, n2, c1, c2):
    angles = angle(n1, n2, 'inches')
    servo1angle = angles[0]
    servo2angle = angles[1]
    servo.append(servo1angle)
    servo2.append(servo2angle)
    if(servo < 0):
        for i in range(int(servo1angle)):
            print(i)
        for i in range(int(servo2angle)):
            print(i)
    
        

#Changes Speed motors travel
def run_servos_G01(n1, n2, c1, c2):
    num1 = (c1-n1)/1.8
    num2 = (c2-n2)/1.8
    for i in range(num1):
        print()
    for i in range(num2):
        print()
    print("G01")

#Incremental Change (If im at 2,2 and we read 5,5 go to 7,7)
#maybe rerun the angle function but the coordinates at the input of the function will just add to the previous ones
def run_servos_G91(n1, n2, c1, c2):
    print("G91")

#Values are in Inches
def run_servos_G20(n1, n2, c1, c2):
    print("G20")

#Values are in Millimeters
#Rerun the angle function but use a convertion 
def run_servos_G21(n1, n2, c1, c2):
    print("G21")

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

coord_dict = {"X":[], "Y":[], "G":[]}
def parse_file():
    #filename = input("What file would you like to run?:  ")
    #file_object = open(filename, "r")
    file_object = open("example.txt", "r")
    for curr_line in file_object:
        curr_line = curr_line.replace(" ","")
        curr_line = curr_line.replace("\n","")
        x_loc = curr_line.find("X")
        y_loc = curr_line.find("Y")
        g_loc = curr_line.find("G")
        coord_dict['Y'].append(curr_line[y_loc+1:])            
        coord_dict['X'].append(curr_line[x_loc+1:y_loc])
        coord_dict['G'].append(curr_line[:x_loc])
    #print(coord_dict)
parse_file()

for i in range(len(coord_dict['X'])):
    #print(int(coord_dict['X'][i]), int(coord_dict['Y'][i]))
    if i != 0:
        if coord_dict['G'][i] == 'G00':
            run_servos_G00(servo[i], servo2[i], servo[i-1], servo2[i-1])
        elif coord_dict['G'][i] == 'G01':
            run_servos_G01(servo[i], servo2[i], servo[i-1], servo2[i-1])
        elif coord_dict['G'][i] == 'G90':
            run_servos_G00(servo[i], servo2[i], servo[i-1], servo2[i-1])
        #elif coord_dict['G'][i] == 'G91':
            #run_servos_G91(servo[i], servo2[i], servo[i-1], servo2[i-1])
        #elif coord_dict['G'][i] == 'G20':
            #run_servos_G20(servo[i], servo[i], servo[i-1], servo2[i-1])
        #elif coord_dict['G'][i] == 'G21':
            #run_servos_G21(servo[i], servo2[i], servo[i-1], servo2[i-1])
        # elif coord_dict['G'][i] == 'M02':
        #     run_servos_M02(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M06':
        #     run_servos_M06(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M72':
        #     run_servos_M72(servo1angle[i], servo2angle[i])
    else:
        if coord_dict['G'][i] == 'G00':
            run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]))
        elif coord_dict['G'][i] == 'G01':
            run_servos_G01(servo[i], servo2[i], servo[i-1], servo2[i-1])
        elif coord_dict['G'][i] == 'G90':
            run_servos_G00(int(coord_dict['X'][i]), int(coord_dict['Y'][i]), int(coord_dict['X'][i-1]), int(coord_dict['Y'][i-1]))
        elif coord_dict['G'][i] == 'G91':
            run_servos_G91(servo[i], servo2[i], servo[i-1], servo2[i-1])
        elif coord_dict['G'][i] == 'G20':
            run_servos_G20(servo[i], servo[i], servo[i-1], servo2[i-1])
        elif coord_dict['G'][i] == 'G21':
            run_servos_G21(servo[i], servo2[i], servo[i-1], servo2[i-1])
        # elif coord_dict['G'][i] == 'M02':
        #     run_servos_M02(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M06':
        #     run_servos_M06(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M72':
        #     run_servos_M72(servo1angle[i], servo2angle[i])
        print(" ")
    
    
    

