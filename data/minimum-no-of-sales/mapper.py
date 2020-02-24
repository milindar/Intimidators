# Reading the data from text file
input = open("data.txt", "r")
#Storing the Mapper output in 01.txt file
output = open("01.txt", "w")

# iterating and getting each line
for line in input:
    # dividing the data using tab seperator
    datalist = line.strip().split("\t")
    # storing the values in variables
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = datalist
    # writing values to output file
    output.write(o + "\t" + r + "\n")

# closing the connection
input.close()
output.close()