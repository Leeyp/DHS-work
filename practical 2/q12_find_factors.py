#find SMALLEST FACTORS
integer = int(input("Input an integer: "))
stop = integer
answers = []
factors = 2
while factors < stop/2 +1:
    if integer % factors == 0:
        answers.append(factors)
        integer /= factors
    else:
        factors += 1
    
print(answers)
