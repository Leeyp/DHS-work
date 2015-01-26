__author__ = 'dhs'

print("{0:10s} {1:s}".format("i", "m(i)"))

for x in range(1,21):
    sum = 0
    for y in range(1,x+1):
        sum += (y/(y+1))
    print("{0:<10} {1:.4f}".format(x, sum))