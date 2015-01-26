__author__ = 'dhs'
from math import floor
def sum_digits(n):
    if n / 10 < 1:
        return int(n)
    else:
        return n % 10 + sum_digits(n/10)

n = float(input("Input number!"))
print(int(sum_digits(n)))