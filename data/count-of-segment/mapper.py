# Reading data from data.txt file and writing into 01.txt file
input = open("data.txt", "r")
output = open("01.txt", "w")
# iterating and reading each line in the data set
for line in input:
    # dividing the data using tab seperator
    datalist = line.strip().split("\t")
    # storing the values in variables
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = datalist
    # writing the output to the 01.txt file
    output.write(h + "\t" + r + "\n")

input.close()
output.close()