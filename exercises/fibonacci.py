__author__ = 'dhs'

def sum_even_fibonacci(num):
    # Write your function code here
    n = 1
    m = 2
    k = 3
    ans = 2
    while k < num:
        n = m
        m = k
        k += n
        if k % 2 == 0:
            ans += k
    return ans

# main
num = 4000000
print(sum_even_fibonacci(num))