__author__ = 'dhs'

def is_prime(number):
    for int in range(2,10):
        if int >= number:
            break
        if number % int == 0:
            return False
    return True

tested = int(input("Input an integer from 1 to 100!"))

if is_prime(tested) == True:
    print(tested, "is a prime number!")
else:
    print(tested, "is not a prime number!")