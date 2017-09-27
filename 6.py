#T Strategy: just number crunching
import math
sum_of_squares = 0
for i in range(1, 101):
	sum_of_squares += math.pow(i, 2)
# Small trick here, using sum 1 to n = n(n+1)/2
square_of_sums = math.pow((100*101/2), 2)
print(int(square_of_sums - sum_of_squares))
