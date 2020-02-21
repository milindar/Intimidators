input = open("purchases.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = datalist
    output.write(paymentType + "\t" + cost + "\n")

input.close()
output.close()