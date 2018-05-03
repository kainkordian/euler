def get_proper_divisors(n):
	return [x for x in range(1,n//2+1) if n % x == 0]

def is_abundant_number(n):
	if n < sum(get_proper_divisors(n)):
		return True
	else: 
		return False

def get_abundant_numbers(i):
	abundant_numbers = set()
	for i in range(1,i):
		if is_abundant_number(i):
			abundant_numbers.add(i)
	return abundant_numbers

abundant_numbers = list(get_abundant_numbers(28123))
sum_of_two_abundant_numbers = {}

outer_index = 0

for a in abundant_numbers:
	for b in abundant_numbers:
		sum_of_them = a + b
		if sum_of_them > 28123:
			break
		sum_of_two_abundant_numbers[sum_of_them] = 0

not_sum_of_two_abundant_numbers = set(range(1,28123)) - set(sum_of_two_abundant_numbers.keys())

print(sum_of_two_abundant_numbers)
print(not_sum_of_two_abundant_numbers)
print(sum(not_sum_of_two_abundant_numbers))