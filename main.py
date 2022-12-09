import random
import math
from functions import *
import time

def mainFunc(filename):
    global dict #made the gui work

    f = open(filename, 'r')
    start_time = time.time()
    random.seed(30)
    #reading first line and taking the floor size
    first_line = f.readline().split()
    first_line = [eval(first_line[x]) for x in range(2,len(first_line))]

    #reading the rest of the lines, ie the clusters
    rest_lines = f.readlines()
    new_lines = []
    components = []

    #creating a list where each index contains a cluster of the compoenents
    for i in rest_lines:
        i = i.split()
        i = [eval(i[x]) for x in range(1,len(i))]
        new_lines.append(i)

    grid = [["--"for x in range(first_line[1])] for y in range(first_line[0])] 
    # print("new lines is" ,new_lines)
    #creating a list where each index has key(unique component)[0] has a unique (x and y)[1]

    x_y = []
    for i in new_lines:

        for x in i:

            if x not in [i[0] for i in (components)]:

                row = random.randrange(first_line[0])
                col = random.randrange(first_line[1])

                while([row,col] in x_y):

                    row = random.randrange(first_line[0])
                    col = random.randrange(first_line[1])

                x_y.append([row,col])
                components.append([x,[row,col]])
                grid[row][col] = x

    print("Grid is ")
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            print("{:<4} " .format(grid[i][j]), end=' ')

        print('\n')

    dict = dict(components)
    # dictcopy2 = dict.copy()

    #all unique components
    cells = [i[0] for i in (components)]

    dict_indx = {}
    for i in cells:

        temp1 = []
        for indx in range(0,len(new_lines)):

            if i in new_lines[indx]:
                temp1.append(indx)

        dict_indx[i] = temp1

    # print("dict is ")
    # print(dict_indx)
    hpl_list = []
    #calculating inital wire length, initial temperature, final temperature
    hpl_list,hpl = hpl_list_init(new_lines,dict)
    #calculating inital wire length, initial temperature, final temperature
    hpl_copy = hpl
    tempinit = hpl * 500
    tempfinal =  (5 * (0.00001)* hpl ) / len(new_lines)

    print("Lenght of hpl list is, ", len(hpl_list))
    print("new_lines list length is , ", len(new_lines))
    print("total is ", sum(hpl_list))
    # 5 * 10^-6 * hpl / number of nets
    
    #printing the inital placement with the wire length
    print("Initial Placement ")
    print_sites(dict,first_line)
    print("total wire length initally is ", hpl)

    #current temp variable
    tempCurrent = tempinit
    moves = 10 * len(cells) # num of moves each temp 
    while (tempCurrent > tempfinal):

        for i in range (0, moves):
            #swap 2 random cells.

            dict_copy = dict.copy()

            x_cell1 = random.randrange(first_line[0])
            y_cell1 = random.randrange(first_line[1])

            x_cell2 = random.randrange(first_line[0])
            y_cell2 = random.randrange(first_line[1])

            cell1 = grid[x_cell1][y_cell1]
            cell2 = grid[x_cell2][y_cell2]

            while( ((x_cell1 == x_cell2) and (y_cell1 == y_cell2)) or (cell1 == "--" and cell2 == "--")):
                x_cell1 = random.randrange(first_line[0])
                y_cell1 = random.randrange(first_line[1])

                x_cell2 = random.randrange(first_line[0])
                y_cell2 = random.randrange(first_line[1])

                cell1 = grid[x_cell1][y_cell1]
                cell2 = grid[x_cell2][y_cell2]

            if (cell1 == "--"):
            
                dict_copy[cell2] = [x_cell1,y_cell1].copy()

                hpl_list_copy,hpl1 = calculate_new_length_one_cell(dict_indx[cell2].copy(),hpl_list.copy(),new_lines,dict_copy)

                if(hpl1 < hpl):
                     # correct swap, so change the old matrix to the one with the swap, and change the HPL
                    dict = dict_copy.copy()
                    grid[x_cell1][y_cell1] = cell2
                    grid[x_cell2][y_cell2] = cell1
                    hpl = hpl1
                    hpl_list = hpl_list_copy.copy()
                else:
                    deltaL = hpl1 - hpl
                    reject_prob = 1 - pow(math.e, -deltaL/tempCurrent)
                    randnumb = random.randint(1, 100)
                    if (randnumb/100 > reject_prob):
                        # accept the change
                        grid[x_cell1][y_cell1] = cell2
                        grid[x_cell2][y_cell2] = cell1
                        dict=dict_copy.copy()
                        hpl_list = hpl_list_copy.copy()
                        hpl = hpl1
                        
            elif(cell2 == "--"):

                dict_copy[cell1] = [x_cell2,y_cell2].copy()

                hpl_list_copy,hpl1 = calculate_new_length_one_cell(dict_indx[cell1].copy(),hpl_list.copy(),new_lines,dict_copy)

                if(hpl1 < hpl):
                    # correct swap, so change the old matrix to the one with the swap, and change the HPL
                    dict = dict_copy.copy()
                    grid[x_cell1][y_cell1] = cell2
                    grid[x_cell2][y_cell2] = cell1
                    hpl = hpl1
                    hpl_list = hpl_list_copy.copy()
                else:
                    deltaL = hpl1 - hpl
                    reject_prob = 1 - pow(math.e, -deltaL/tempCurrent)
                    randnumb = random.randint(1, 100)
                    if (randnumb/100 > reject_prob):
                        # accept the change
                        grid[x_cell1][y_cell1] = cell2
                        grid[x_cell2][y_cell2] = cell1
                        dict=dict_copy.copy()
                        hpl_list = hpl_list_copy.copy()
                        hpl = hpl1
                        

            else:
                dict_copy[cell1] = [x_cell2,y_cell2].copy()
                dict_copy[cell2] = [x_cell1,y_cell1].copy()

                hpl_list_copy,hpl1 = calculate_new_length_two_cell(list(set(dict_indx[cell1].copy() + dict_indx[cell2].copy())),hpl_list.copy(),new_lines,dict_copy)

                if(hpl1 < hpl):
                    # correct swap, so change the old matrix to the one with the swap, and change the HPL
                    dict = dict_copy.copy()
                    grid[x_cell1][y_cell1] = cell2
                    grid[x_cell2][y_cell2] = cell1
                    hpl = hpl1
                    hpl_list = hpl_list_copy.copy()
                else:
                    deltaL = hpl1 - hpl
                    reject_prob = 1 - pow(math.e, -deltaL/tempCurrent)
                    randnumb = random.randint(1, 100)
                    if (randnumb/100 > reject_prob):
                        # accept the change
                        grid[x_cell1][y_cell1] = cell2
                        grid[x_cell2][y_cell2] = cell1
                        dict= dict_copy.copy()
                        hpl_list = hpl_list_copy.copy()
                        hpl = hpl1
                        # print new matrix
                        # print_sites(dict, first_line)

        #reduce temp (cooling factor)
        tempCurrent = tempCurrent * 0.95

    
    print("FINAL PLACEMENT")
    print_sites(dict, first_line) # final placement.
    print("Total wire length = " + str(hpl))
    print(" {} seconds" .format(time.time() - start_time))
    return first_line,dict,hpl,hpl_copy