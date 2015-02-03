__author__ = 'dhs'

def is_prime(a):
    return all(a % i for i in range(2, a))

try:
    infile = open("PRIME.IN", "r")
    n = infile.readlines()
    outfile = open("PRIME.OUT", "w")
    outfile.write(is_prime(n))

except IOError:
    print("Error detected")