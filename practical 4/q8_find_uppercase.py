__author__ = 'dhs'

def find_uppercase(str):
    upper = 0
    for x in str:
        if x.isupper():
            upper += 1
    return upper

str = input("Input string for me to count uppercases: ")

print(find_uppercase(str))