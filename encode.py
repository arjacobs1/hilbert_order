#!/usr/bin/env python3

# encode.py
# Implementation of encoding and decoding algorithms as described in
# "A new algorithm for encoding and decoding the Hilbert order" by Ningtao
# Chen, Nengchao Wang, and Baochang Shi
#
# Chen, N., Wang, N., & Shi, B. (2007). A new algorithm for encoding and
# decoding the Hilbert order. Software-Practice and Experience, 37(8), 897-908.


import math
import sys

def getQuadrant(x, y, rmin):
    mwidth = 2**(rmin)   # matrix width
    qwidth = 2**(rmin-1) # quadrant width
    if ((0 <= x) and (x < qwidth)) and ((0 <= y) and (y < qwidth)):
        return 0
    elif ((0 <= x) and (x < qwidth)) and ((qwidth <= y) and (y < mwidth)):
        return 1
    elif ((qwidth <= x) and (x < mwidth)) and ((qwidth <= y) and (y < mwidth)):
        return 2
    else:
        return 3

if not len(sys.argv) == 4:
    print("Usage: provide x, y, and n as command line arguments.")
    quit()

# ----- INITIALIZATION -----
x = int(sys.argv[1])
y = int(sys.argv[2])
n = int(sys.argv[3])

z = ""

if (x==0) and (y==0):
    rmin = 1
else:
    rmin = int(math.floor(math.log(int(max(x,y)), 2)) + 1)

w = 2**(rmin-1)


# if parities of n and rmin do not match, swap x and y
if not rmin%2 == n%2:    
    tmp = x
    x = y
    y = tmp


# ----- ITERATION -----
while not rmin == 0:
    Q = getQuadrant(x, y, rmin)
    z += str(Q)
    if (Q == 0):
        tmp = x
        x = y
        y = tmp
    elif (Q == 1):
        y = y - w
    elif (Q == 2):
        x = x - w
        y = y - w
    else:
        tmp = x
        x = w - y - 1 
        y = (w*2) - tmp - 1

    rmin = rmin - 1
    w = w / 2

print (z)
