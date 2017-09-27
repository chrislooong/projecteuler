# Strategy: store primes and to check if next is a prime iterate through known primes to see if new candidate is prime
# Much faster method is to use sieve of eratosthenes to remove all unneeded nums up to the prime number approximation, n/log(n) density
# First solution is sufficiently fast so not overengineering, here
primes = []
candidate = 1
while len(primes) < 10001:
    candidate += 1
    is_prime = True
    for prime in primes:
        if candidate % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
print(candidate)
