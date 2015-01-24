__author__ = 'dhs'
x = 1
while x != 0:
    integer = input("Input an integer from 0 to 1000")

    if 0 <= int(integer) <= 1000:
        cheat_method = []
        for digits in range(0,len(integer)):
            cheat_method.append(int(integer[digits]))
        sum_digits = sum(cheat_method)
        print(sum_digits)

    else:
        print("That was not between 0 to 1000!")