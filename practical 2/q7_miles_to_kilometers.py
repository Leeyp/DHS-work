print("Miles Kilometers Kilometers Miles")
for x in range(1,11):
    otherline = x*5
    print("{0:<5} {1:<10} {2:<10} {3:<.5}".format(
        x, x*1.609, otherline+15, (otherline+15)/1.609))
