import random

#iterating through every cluster(net) which is in new_lines
#calculating the hpl of each cluster and appending it to a list to later on get the total
def calculate_total_length(new_lines, dict):

    hpl = 0
    for net in new_lines:
        x_lst = []
        y_lst = []

        for comp in net:

            x_lst.append(dict[comp][0])
            y_lst.append(dict[comp][1])

        xmin = min(x_lst)
        xman = max(x_lst)

        ymin = min(y_lst)
        ymax = max(y_lst)

        length = (xman-xmin) + (ymax-ymin)

        hpl += length

    return hpl

def print_sites(dict,first_line):
    #initialzing the 2D array (site)
    Matrix = [['--' for x in range(first_line[1])] for y in range(first_line[0])] 

    #filling up the 2D array
    for i,z in dict.items():
        Matrix[z[0]][z[1]] = i

    #visualzing the inital placement
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix[0])):
            print("{:<4} " .format(Matrix[i][j]), end=' ')

        print('\n')


def swap(cells,hpl_old,dict,new_lines):

    dict_copy = dict.copy()
    temp1 = random.randrange(len(cells))
    temp2 = random.randrange(len(cells))
    while(temp1 == temp2):
        temp1 = random.randrange(len(cells))
        temp2 = random.randrange(len(cells))

    tempdict1 = dict_copy[cells[temp1]]
    tempdict2 = dict_copy[cells[temp2]]

    dict_copy[cells[temp1]] = tempdict2
    dict_copy[cells[temp2]] = tempdict1


    hpl1 = calculate_total_length(new_lines,dict_copy)

    if(hpl1 < hpl_old):
        dict = dict_copy.copy()
        lower_hpl = True
    else:
        lower_hpl = False


    return lower_hpl,dict,dict_copy,hpl1

