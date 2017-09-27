# Store known primes and iterate over all primes lower than sqrt(2000000), since elements
#   above that would be p | p*q = k, where q is lower than sqrt(2000000) and so has been hit
import math
known_primes = []
candidate_prime = 2
prime_total = 0
while candidate_prime < 2000000:
    is_prime = True
    for prime in known_primes:
        if candidate_prime % prime == 0:
            is_prime = False
        if prime > math.sqrt(2000000):
            break
    if is_prime:
        known_primes.append(candidate_prime)
        prime_total += candidate_prime
    candidate_prime += 1
print(prime_total)
