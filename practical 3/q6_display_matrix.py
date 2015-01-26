__author__ = 'dhs'
import random

n = int(input("Input size of matrix: "))

for row in range(n):
    for column in range(n):
        print(random.randint(0,1), end=" ")
    print(" ")