import math
import pyfirmata
import time
from pyfirmata import Arduino, util
board = pyfirmata.Arduino('COM6');
unitType = "in";
movementType = "abs";
currLoc = [0,0,0];
speed = 0;
SA1 = 0;
SA2 = 0;


def welcome():
    file = input('What file would you like to run?:    ')
    return file

#Used to parse and seperate the G code file into correst peicess
def openFile(FileName):
    f = open(FileName)
    return f

def runMotorsTo(motorAngle1, motorAngle2, speedIn):
    #rate 1.8 degrees per step
    if(speedIn == 0):
        speedIn = 1;
    if(speedIn > 100):
        speedIn = 100;
    if(speedIn < 1):
        speedIn = 1;
    
    speedIn = speedIn/100;
    steps1 = motorAngle1 * 2000;
    steps2 = motorAngle2 * 200;
    
    if(steps1 < 0):
        steps1 = steps1 * -1;
        board.digital[5].write(1);
    else:
        board.digital[5].write(0);
    if(steps2 < 0):
        steps2 = steps2 * -1;
        board.digital[6].write(1);
    else:
        board.digital[6].write(0);
    for i in range(0, steps1):
        board.digital[2].write(1);
        time.sleep(0.001*speedIn);
        board.digital[2].write(0);
        time.sleep(0.001*speedIn);
    for i in range(0, steps2):
        board.digital[3].write(1);
        time.sleep(0.0001*speedIn);
        board.digital[3].write(0);
        time.sleep(0.0001*speedIn);
    return;
    




def inverseKinematics(x, y, z, speedIn):
    a1 = 193.675
    a2 = 193.675
    SA1 = math.atan2(y, x)
    SA2 = math.acos((x**2 + y**2 + z**2 - a1**2 - a2**2)/(2*a1*a2))
    runMotorsTo(SA1, SA2, speedIn)

    
    







def SLmove(line, extrude):
    #rate 1.8 degrees per step
    if(movementType == "abs"):
        if(unitType == "in"):
            currLoc[0] = float(line[1:line.find('Y')]) * 25.4;
            currLoc[1] = float(line[line.find('Y')+1:line.find('Z')]) * 25.4;
            currLoc[2] = float(line[line.find('Z')+1:line.find('F')]) * 25.4;
            speed = float(line[line.find('F')+1:]);
        else: #unitType == "mm"
            currLoc[0] = float(line[1:line.find('Y')]);
            currLoc[1] = float(line[line.find('Y')+1:line.find('Z')]);
            currLoc[2] = float(line[line.find('Z')+1:line.find('F')]);
            speed = float(line[line.find('F')+1:]);
    elif(movementType == "rel"):
        if(unitType == "in"):
            x = float(line[1:line.find('Y')]) * 25.4;
            y = float(line[line.find('Y')+1:line.find('Z')]) * 25.4;
            z = float(line[line.find('Z')+1:line.find('F')]) * 25.4;
            speed = float(line[line.find('F')+1:]);
            currLoc[0] += x;
            currLoc[1] += y;
            currLoc[2] += z;
        else: #unitType == "mm"
            x = float(line[1:line.find('Y')]);
            y = float(line[line.find('Y')+1:line.find('Z')]);
            z = float(line[line.find('Z')+1:line.find('F')]);
            speed = float(line[line.find('F')+1:]);
            currLoc[0] += x;
            currLoc[1] += y;
            currLoc[2] += z;
    #move to new location
    inverseKinematics(currLoc[0], currLoc[1], currLoc[2], speed);
    
    
    
    
    
    
#def Cmove(line, dir):
    

def changeTool(tool):
        if tool == "T1":
                board.digital[9].write(42)
        elif tool == "T2":
                board.digital[9].write(90)
        elif tool == "T3":
                board.digital[9].write(137)
        else:
                #do nothing
                print("")
        return



def parse(line):
    if(line[0] == 'G'):
        match line[1:2]:
            case '00':
                #straight line move w/o extrusion
                SLmove(line, 0);
                
            case '01':
                #straight line move w/ extrusion 
                SLmove(line, 1);
            #case '02':
                #clockwise arc
                #Cmove(line, 0);
            #case '03':
                #counterclockwise arc
                #Cmove(line, 1);
            case '20':
                unitType = "in";
            case '21':
                unitType = "mm";
            case '90':
                movementType = "abs";
            case '91':
                movementType = "rel";
                
    elif(line[0] == 'M'):
        match line[1:3]:
            case '6':
                changeTool(line[3:]);
                #tool change
    else:
        print(line);
        
                
                
            
            
            

def main():
    inputFile = welcome();
    f = openFile(inputFile);
    GCArr = f.readlines();
    fileLength = len(GCArr);
    iterator = 0;
    while( fileLength != 0):
        parse(GCArr[iterator]);
        iterator = iterator + 1;
        fileLength = fileLength - 1;
    
        
    
    









    #print(coord_dict)

#Uses inverse kinematics to determine the desired angle based on coordinates
