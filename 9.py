# Strategy: find a,b,c through brute force iteration then print their product
import sys
import math
for a in range(1,1000):
    for b in range(a,1000):
        if math.pow(a, 2) + math.pow(b, 2) == math.pow(1000-a-b, 2):
            print(a*b*(1000-a-b))
            sys.exit(0)
