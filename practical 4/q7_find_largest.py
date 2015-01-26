__author__ = 'dhs'

def find_largest(alist):
    if len(alist) == 1:
        return alist
    else:
        return max(alist)
x = 2
list = []
while x == 2:
    integer = int(input("Input integers into a list. Terminate with -1: "))
    if integer == -1:
        break
    else:
        list.append(integer)

print(find_largest(list))