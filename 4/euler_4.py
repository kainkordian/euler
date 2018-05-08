upper_limit = 999
lower_limit = 100
largest_palindrome = 0
for a in range(upper_limit, lower_limit-1, -1):
	for b in range(upper_limit, lower_limit-1, -1):
		prod = str(a * b)
		if (prod == prod[::-1]) & (largest_palindrome < (a*b)):
			print(prod)
			print(upper_limit)
			print(lower_limit)
			largest_palindrome = a*b
			lower_limit = b
			upper_limit = a

print(upper_limit)
print(lower_limit)
print(prod)
