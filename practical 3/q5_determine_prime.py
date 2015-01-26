__author__ = 'dhs'

def is_prime(a):
    return all(a % i for i in range(2, a))

row = []
counter = 0
for x in range(2,9999999):
    if len(row) == 10:
        print("{0:<5} {1:<5} {2:<5} {3:<5} {4:<5} {5:<5} {6:<5} {7:<5} {8:<5} {9:<5}"
    .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        counter += 1
        row = []
    if is_prime(x):
        row.append(x)
    if counter == 100:
        break

