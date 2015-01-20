__author__ = 'dhs'

x = 1
numbers = []
while x != 0:
    integers = int(input("Input an integer"))
    if integers == -1:
        break
    numbers.append(integers)

print(sum(numbers))