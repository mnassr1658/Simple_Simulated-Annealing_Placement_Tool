import random
import math
from functions import *


def mainFunc(filename):
    global dict #made the gui work

    f = open(filename, 'r')

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


    dict = dict(components)
    dictcopy2 = dict.copy()

    #all unique components
    cells = [i[0] for i in (components)]

    #calculating inital wire length, initial temperature, final temperature
    hpl = calculate_total_length(new_lines,dict)
    hpl_copy = hpl
    tempinit = hpl * 500
    tempfinal =  (5 * (0.00001)* hpl ) / len(new_lines)
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
            do_we_accept,dict1,dict_copy,hpl_new,hpl = swap(cells,hpl,dict,new_lines)



            if(do_we_accept):
                # correct swap, so change the old matrix to the one with the swap, and change the HPL
                dict=dict1.copy()
                hpl = hpl_new
                # print the new matrix
                # print_sites(dict, first_line)
            else:
                deltaL = hpl_new - hpl
                reject_prob = 1 - pow(math.e, -deltaL/tempCurrent)
                randnumb = random.randint(1, 100)
                if (randnumb/100 > reject_prob):
                    # accept the change
                    dict=dict1.copy()
                    hpl = hpl_new
                    # print new matrix
                    # print_sites(dict, first_line)


        #reduce temp (cooling factor)
        tempCurrent = tempCurrent * 0.95

    
    print("FINAL PLACEMENT")
    print_sites(dict, first_line) # final placement.
    print("Total wire length = " + str(hpl))

    return first_line,dict,hpl,hpl_copy
