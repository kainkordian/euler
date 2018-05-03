import numpy as np
def get_proper_divisors(n):
	if n == 1:
		return [1]
	proper_divisors = [1,n]
	for x in range(2, int(np.sqrt(n))):
		if n % x == 0:
			proper_divisors.append(x)
			proper_divisors.append(n//x)
	return proper_divisors

triangle_number = 0
n = 1
biggest_amount_so_far = 0

while True:
	triangle_number += n
	amount_of_proper_divisors = 2 + len(get_proper_divisors(triangle_number))
	n += 1
	if amount_of_proper_divisors > biggest_amount_so_far:
		biggest_amount_so_far = amount_of_proper_divisors
	if amount_of_proper_divisors > 500:
		break

print(biggest_amount_so_far)
print(triangle_number)