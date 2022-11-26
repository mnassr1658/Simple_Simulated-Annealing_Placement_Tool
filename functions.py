import random

#iterating through every cluster(net) which is in new_lines
#calculating the hpl of each cluster and appending it to a list to later on get the total
def calculate_total_length(new_lines, dict):
    #new lines has the nets, and dict is the grid
    hpl = 0
    for net in new_lines:
        x_lst = []
        y_lst = []
        # lists to hold x and y coordinates for each cell in each net
        for comp in net:

            x_lst.append(dict[comp][0])
            y_lst.append(dict[comp][1])
            #gets the x and y coordinate for each cell

        xmin = min(x_lst)
        xman = max(x_lst)

        ymin = min(y_lst)
        ymax = max(y_lst)
        
        #calculate delta x and delta y to get hpl of this net

        length = (xman-xmin) + (ymax-ymin)

        hpl += length
        #final hpl is the summation of all net hpls.

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
    #gets 2 random indices to be switched, in case they are the same, do it again.
    temp1 = random.randrange(len(cells)) #in range of numb of cells in the list itself to garauntee correctness
    temp2 = random.randrange(len(cells))
    while(temp1 == temp2):
        temp1 = random.randrange(len(cells))
        temp2 = random.randrange(len(cells))

    #get x and y coordinates of each cell
    tempdict1 = dict_copy[cells[temp1]]
    tempdict2 = dict_copy[cells[temp2]]

    #swap the coordinates
    dict_copy[cells[temp1]] = tempdict2
    dict_copy[cells[temp2]] = tempdict1

    # get the new HPL with the new dictionary
    hpl1 = calculate_total_length(new_lines,dict_copy)

    # if hpl is less, then the swap is favoured
    if(hpl1 < hpl_old):
        dict = dict_copy.copy()
        lower_hpl = True
    else:
        lower_hpl = False
        #else, swap is not favoured


    return lower_hpl,dict,dict_copy,hpl1, hpl_old