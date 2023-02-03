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
x = 7
y = -7
angles = angle(x,y)
print(angles)
x = 4
y = 2
angles = angle(x,y)
print(angles)
x = 5
y = 9
angles = angle(x,y)
print(angles)