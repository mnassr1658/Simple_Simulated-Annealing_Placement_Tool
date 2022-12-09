import random


def calculate_new_length_one_cell(indx_list,hpl_list,new_lines, dict):

    for i in indx_list:
        x_lst = []
        y_lst = []

        for comp in new_lines[i]:

            x_lst.append(dict[comp][0])
            y_lst.append(dict[comp][1])
            
        length = (max(x_lst)-min(x_lst)) + (max(y_lst)-min(y_lst))

        hpl_list[i] = length
    
    return hpl_list,sum(hpl_list)

def calculate_new_length_two_cell(indx_list,hpl_list,new_lines, dict):

   
    for i in indx_list:
        x_lst = []
        y_lst = []

        for comp in new_lines[i]:

            x_lst.append(dict[comp][0])
            y_lst.append(dict[comp][1])

        length = (max(x_lst)-min(x_lst)) + (max(y_lst)-min(y_lst))

        hpl_list[i] = length

    return hpl_list,sum(hpl_list)


def hpl_list_init(new_lines, dict):

    hpl = 0
    hpl_list = []
    for i in range(0,len(new_lines)):
        x_lst = []
        y_lst = []

        for comp in new_lines[i]:

            x_lst.append(dict[comp][0])
            y_lst.append(dict[comp][1])

        length = (max(x_lst)-min(x_lst)) + (max(y_lst)-min(y_lst))

        hpl_list.append(length)
        hpl += length

    return hpl_list,hpl

def print_sites(dict,first_line):
    #initialzing the 2D array (site)
    Matrix = [['1' for x in range(first_line[1])] for y in range(first_line[0])] 

    #filling up the 2D array
    for i,z in dict.items():
        Matrix[z[0]][z[1]] = '0'

    #visualzing the inital placement
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix[0])):
            print("{:<4} " .format(Matrix[i][j]), end=' ')

        print('\n')
