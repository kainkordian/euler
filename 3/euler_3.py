solve_for = 600851475143
primes = set([])
n = solve_for
x = 2
while x <= n:
	is_prime = True
	for p in primes:
		if x % p == 0:
			is_prime = False
	if is_prime:
		primes.add(x)
		while n % x == 0:
			n = n // x
			print(str(x) + ", " + str(n))
	x += 1

print(primes)
print(x-1)
