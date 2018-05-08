def primes_up_to(n):
	numbers = set(range(2,n))
	primes = set()
	while numbers:
		p = min(numbers)
		primes.add(p)
		numbers = numbers - set(range(p,n,p))
		print(len(numbers))
	return primes

n = int(input("Which n you want the primes up to?"))
print(sum(primes_up_to(n)))