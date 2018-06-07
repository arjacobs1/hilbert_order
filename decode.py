#!/usr/bin/env python3

# decode.py
# Implementation of encoding and decoding algorithms as described in
# "A new algorithm for encoding and decoding the Hilbert order" by Ningtao
# Chen, Nengchao Wang, and Baochang Shi
#
# Chen, N., Wang, N., & Shi, B. (2007). Efficient algorithm for encoding and
# decoding the Hilbert order. Software-Practice and Experience, 37(8), 897-908.

import math
import sys

if not len(sys.argv) == 3:
    print("Usage: provide z and n as command line arguments.")
    quit()

# ----- INITIALIZATION -----
z = str(sys.argv[1])
n = int(sys.argv[2])

r = z[-1:]
z = z[:-1]
w = 2

if r == "0":
    x = 0; y = 0
elif r == "1":
    x = 0; y = 1
elif r == "2":
    x = 1; y = 1
else:
    x = 1; y = 0


# ----- ITERATION -----
while len(z) > 0:
    r = z[-1:]
    z = z[:-1]
    if r == "0":
        tmp = x
        x = y
        y = tmp
    elif r == "1":
        y = y + w
    elif r == "2":
        x = x + w
        y = y + w
    else:
        tmp = x
        x = (w*2)-y-1
        y = w-tmp-1
    w = w*2


if (x==0) and (y==0):
    rmin = 1
else:
    rmin = int(math.floor(math.log(int(max(x,y)), 2)) + 1)

if not rmin%2 == n%2:
    tmp = x
    x = y
    y = tmp

print ("(",x,",",y,")")
