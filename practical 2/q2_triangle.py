x = 1
while x != 0:
    valid = "no"
    sides = []
    for side in range(0,3):
        print("Enter side", side+1)
        sides.append(int(input(" ")))
                         
    a = sides[0] + sides[1]
    b = sides[1] + sides[2]
    c = sides[0] + sides[2]
    if a > sides[2]:
        if b > sides[0]:
                if c > sides[1]:
                         valid = "yes"
    else:
                         valid = "no"

    if valid == "yes":
                         print("Perimeter =", sum(sides))
    elif valid == "no":
                         print("Invalid Triangle!")
