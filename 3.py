# Strategy: divide out divisors. When a candidate number is a divisor it is guatanteed 
# to be prime since composite numbers' divisors are already hit and divided out
# also we are guaranteed to hit the prime which is greater or equal to the primes 
# already hit because if it were not it would have been hit on a previous iteration
num = 600851475143
candidate = 2
while candidate != num:
	if num % candidate == 0:
		num /= candidate
		continue
	candidate += 1
print(candidate)
