primes = set()
n = 2
i = 0
while i < 10001:
	is_prime = True
	for p in primes:
		if n % p == 0:
			is_prime = False
			break
	if is_prime:
		primes.add(n)
		i += 1
	n += 1

print(i, n-1)