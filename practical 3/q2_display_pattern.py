__author__ = 'dhs'

def display_pattern(n):
    for x in range(n):
        pattern= []
        for y in range(x+1, 0, -1):
            pattern.append(str(y))

        print("{0:>s}".format(' '.join(pattern)))
        #don't know how to display n characters
        #{0:>ns} doesn't work!

n = int(input("Input the n! "))

print(display_pattern(n))