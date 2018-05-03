def get_proper_divisors(n):
	proper_divisors = [x if x % n == 0 for x in range(1,n//2)]
	proper_divisors.append(n)
	return proper_divisors
