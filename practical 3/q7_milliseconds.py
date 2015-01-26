__author__ = 'dhs'

def prntime(ms):
    s=ms/1000
    m,s=divmod(s,60)
    h,m=divmod(m,60)
    return h,m,s

milliseconds = int(input("Input milliseconds: "))

print('%dh:%dm:%ds' % prntime(milliseconds))