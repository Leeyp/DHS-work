a = int(input("Input number 1: "))
b = int(input("Input number 2: "))
d = min(a,b)
while d != 0:
    if a % d == 0:
        if b % d == 0:
            print(d)
            break
    d -= 1
