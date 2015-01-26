__author__ = 'dhs'

def sum_series(i):
    if i == 1:
        return 1
    else:
        return 1/i + sum_series(i-1)

i = int(input("Input i: "))

print(sum_series(i))