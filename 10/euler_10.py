upper_limit = 2000000

primes = set()

for i in range(2, upper_limit):
	if i % 20000 == 0:
		print(str(i // 20000) + "%, " + str(len(primes)) + " primes found")
	is_prime = True
	for p in primes:
		if i % p == 0:
			is_prime = False
			break
	if is_prime:
		primes.add(i)

# print(primes)
print(sum(primes))