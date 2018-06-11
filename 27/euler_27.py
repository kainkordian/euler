import time

def sieve_of_erathostenes(n):
	primes = [True] * n
	primes[0] = primes[1] = False
	for (i, is_prime) in enumerate(primes):
		if is_prime:
			yield i
			for k in range(i*i, n, i):
				primes[k] = False

def takeWhile(elements, condition):
	result_list = []
	for e in elements:
		if condition(e):
			result_list.append(e)
		else:
			break
	return result_list

def isPrime(value, primes):
	return value in primes

def main(argv=None):
	start = time.time()
	primes = {}
	primes_list = []
	for p in sieve_of_erathostenes(argv):
		primes[p] = True
		primes_list.append(p)
	a_list = range(-999,1000)
	b_list = takeWhile(primes_list, (lambda x: x < 1001))
	super_coefficients = (0,0)
	product_of_super_coeff = 0

	longest_prime_series = 0
	for b in b_list:
		for a in a_list:
			n = 0
			while True:
				if n*n + n*a + b in primes:
					n += 1
				else:
					if n > longest_prime_series:
						longest_prime_series = n
						product_of_super_coeff = a*b
						super_coefficients = (a,b)
					break

	end = time.time()
	print(argv)
	print("Seconds passed: " + str(end - start))
	print("Length of longest prime series: " + str(longest_prime_series))
	print("super coefficients: " + str(super_coefficients))
	print("Product of super coefficients: " + str(product_of_super_coeff))

if __name__ == "__main__":
	# The biggest prime number can only be 2001000, when we maximize b and set n = b
	main(2001001)