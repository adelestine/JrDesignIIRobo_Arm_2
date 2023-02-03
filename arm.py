import math

def run_servos_G00(n1, n2):
    print("G00")
def run_servos_G01(n1, n2):
    print("G01")
def run_servos_G90(n1, n2):
    print("G90")
def run_servos_G91(n1, n2):
    print("G91")
def run_servos_G20(n1, n2):
    print("G20")

def run_servos_G21(n1,n2):
    print("G21")

def angle(x,y):
    L = 5.25
    hypotnuse = math.sqrt(pow(x,2) + pow(y,2))
    s1 = hypotnuse/2
#print(x,y)
#print(pow(L,2),pow(s1,2))
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
    print(coord_dict)


parse_file()
servo = []
servo2 = []
for i in range(len(coord_dict['X'])):
    print(int(coord_dict['X'][i]), int(coord_dict['Y'][i]))
    angles = angle(int(coord_dict['X'][i]), int(coord_dict['Y'][i]))
    servo1angle = angles[0]
    servo2angle = angles[1]
    servo.append(servo1angle)
    servo2.append(servo2angle)

print(servo, servo2)
for i in range(len(servo)):
    if i != 0:
        if coord_dict['G'][i] == 'G00':
            run_servos_G00(servo[i], servo2[i])
        elif coord_dict['G'][i] == 'G01':
            run_servos_G01(servo[i], servo2[i])
        elif coord_dict['G'][i] == 'G90':
            run_servos_G90(servo[i], servo2[i])
        elif coord_dict['G'][i] == 'G91':
            run_servos_G91(servo[i], servo2[i])
        elif coord_dict['G'][i] == 'G20':
            run_servos_G20(servo[i], servo[i])
        elif coord_dict['G'][i] == 'G21':
            run_servos_G21(servo[i], servo2[i])
        # elif coord_dict['G'][i] == 'M02':
        #     run_servos_M02(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M06':
        #     run_servos_M06(servo1angle[i], servo2angle[i])
        # elif coord_dict['G'][i] == 'M72':
        #     run_servos_M72(servo1angle[i], servo2angle[i])
    else:
        print('hello')
    
    
    

