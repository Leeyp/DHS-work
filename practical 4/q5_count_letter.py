__author__ = 'dhs'

def count_letter(str, ch):
    count = 0
    for x in range(len(str)):
        if str[x] == ch:
            count += 1
    return count

str = input("Input string: ")
ch = input("Input ch: ")

print(count_letter(str,ch))