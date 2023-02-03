import math

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

#name = input("What file would you like to run?:   ")
name = 'example.txt'
file_object = open(name, "r")
num_lines = len(file_object.readlines())
file_object.close()

file_object = open(name, 'r')
xcommands = []
ycommands = []
for i in range(num_lines):
    file_object.readline(5)
    xcommands.append(file_object.readline(3))
    file_object.readline(2)
    ycommands.append(file_object.readline())
file_object.close()
#print(xcommands)
#print(ycommands)



for i in range(num_lines):
    xcommands[i] = xcommands[i].replace(' ', '')
    ycommands[i] = ycommands[i].replace(' ', '')
    xcommands[i] = xcommands[i].replace('\n', '')
    ycommands[i] = ycommands[i].replace('\n', '')
    if xcommands[i] == '':
        xcommands[i] = xcommands[i-1]
    if ycommands[i] == '':
        ycommands[i] = ycommands[i-1]

file_object.close()
#print(xcommands)
#print(ycommands)

servo = []
servo2 = []
for i in range(num_lines):
    angles = angle(int(xcommands[i]), int(ycommands[i]))
    servo1angle = angles[0]
    servo2angle = angles[1]
    servo.append(servo1angle)
    servo2.append(servo2angle)

print(servo, servo2)

