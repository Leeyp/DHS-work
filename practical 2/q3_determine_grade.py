x = 1
while x != 0:
    score = int(input("Enter score: "))

    if 0 <= score <= 100:
                if 70 <= score <= 100:
                    print("A")
                elif 60 <= score <= 69:
                    print("B")
                elif 55 <= score <= 59:
                    print("C")
                elif 50 <= score <= 54:
                    print("D")
                elif 45 <= score <= 49:
                    print("E")
                elif 35 <= score <= 44:
                    print("S")
                else:
                    print("U")
    else:
        print("Invalid! Score must be within 0 - 100.")
