# Strategy: multiply numbers of form p^k where p prime and k largest num | p^k <= 20

import math
result = 1
for i in range(2, 21):
	# Only care if is prime
	is_prime = True
	for j in range(2,i):
		if i % j == 0:
			is_prime = False
	if not is_prime:
		continue
	# See what is the largest number prime^k less than 20
	k = 1
	# Increment power until next is higher than 20
	while math.pow(i, k + 1) < 20:
		k += 1
	result *= math.pow(i, k)
print(int(result))
