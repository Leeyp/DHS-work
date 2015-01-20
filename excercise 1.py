__author__ = 'dhs'

x = int(input("Give me the number of numbers that you will key in: "))
numbers = []
while x != 0:
    integers = int(input("Input an integer"))
    numbers.append(integers)
    x -= 1

print(sum(numbers))
