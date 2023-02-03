

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
    print(coord_dict)
