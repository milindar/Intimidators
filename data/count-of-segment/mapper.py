input = open("data.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = datalist
    output.write(h + "\t" + r + "\n")

input.close()
output.close()