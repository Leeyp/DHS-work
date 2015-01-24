integer = int(input("Input an integer: "))
answers = []

for i in range(1, int(integer**0.5) + 1):
    if integer % i == 0:
        answers.append(i)
        answers.append(int(integer/i))

print(sorted(answers))
