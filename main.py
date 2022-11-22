import random
from functions import *



f = open("d0.txt", 'r')

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

# print(new_lines)
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

#all unique components
cells = [i[0] for i in (components)]

#calculating inital wire length
hpl = calculate_total_length(new_lines,dict)

#initialzing the 2D array (site)
Matrix = [['--' for x in range(first_line[1])] for y in range(first_line[0])] 

#filling up the 2D array
for i,z in dict.items():
    Matrix[z[0]][z[1]] = i


#printing the inital placement with the wire length
print_sites(Matrix)
print("total wire length initally is ", hpl)


do_we_accept,dict,dict_copy,hpl = swap(cells,hpl,dict,new_lines)

#printing if we swapped or not and new placement
print("total wire length after swap is ", hpl)
print("swap is ", do_we_accept)

#initialzing the 2D array (site)
Matrix1= [['--' for x in range(first_line[1])] for y in range(first_line[0])] 

#filling up the 2D array
for i,z in dict.items():
    Matrix1[z[0]][z[1]] = i

print_sites(Matrix1)



