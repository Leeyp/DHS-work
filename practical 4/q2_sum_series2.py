__author__ = 'dhs'

def sum_series(i):
    if i == 1:
        return i/(2*i+1)
    else:
        return i/(2*i+1) + sum_series(i-1)

i = int(input("Input i: "))

print(sum_series(i))