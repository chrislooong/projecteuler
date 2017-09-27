import math
fib1 = 1
fib2 = 2
total = 2
while fib2 < 4000000:
	fib3 = fib1 + fib2
	if fib3 % 2 == 0:
		total += fib3
	fib1 = fib2
	fib2 = fib3
print(total)
