__author__ = 'dhs'
import re

def check_alphabet(nric):
    sum = int(nric[1])*2
    sum += int(nric[2])*7
    sum += int(nric[3])*6
    sum += int(nric[4])*5
    sum += int(nric[5])*4
    sum += int(nric[6])*3
    sum += int(nric[7])*2
    if nric[0] in ["t","T", "g", "G"]:
        sum += 4
    checksum = sum % 11
    print(checksum)
    if checksum == 1:
        return "A"
    elif checksum == 2:
        return "B"
    elif checksum == 3:
        return "C"
    elif checksum == 4:
        return "D"
    elif checksum == 5:
        return "E"
    elif checksum == 6:
        return "F"
    elif checksum == 7:
        return "G"
    elif checksum == 8:
        return "H"
    elif checksum == 9:
        return "I"
    elif checksum == 10:
        return "Z"
    elif checksum == 0:
        return "J"

nric = input("Input NRIC")

pattern = re.compile("^[sSTtFfGg][0-9]{7}[a-zA-Z]$")

if not pattern.match(nric):
    print("Invalid NRIC")

else:
    print(nric[0:9])
    print(nric[8])
    print(check_alphabet(nric))
    if nric[8] == check_alphabet(nric):
        print("ok")
    else:
        print("Invalid Check Digit")
