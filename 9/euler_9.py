def is_pythagorean(a,b,c):
	return ((a*a + b*b) == c*c)

def find_pythagorean_triple(n):
	for a in range(1,n):
		print(a)
		for b in range(1,n):
			for c in range(1,n):
				if (a+b+c) >= n:
					if (a+b+c) == n:
						if is_pythagorean(a,b,c):
							print()
							print(a,b,c)
							print(a*b*c)
							return "Success!"
					else:
						break

find_pythagorean_triple(1000)