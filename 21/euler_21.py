import time
import numpy as np

def get_sum_of_proper_divisors(n):
	result = 1
	for x in range(2,int(np.sqrt(n))+1):
		if n % x == 0:
			result += x
			if x != n // x:
				result += n // x
	return result

def get_dict_of_proper_divisor_sums(until):
	n_to_sum = {}
	dict_of_sums = {}
	for n in range(1,until):
		sum_of_them = get_sum_of_proper_divisors(n)
		n_to_sum[n] = sum_of_them
		dict_of_sums[sum_of_them] = 0
	return  n_to_sum, dict_of_sums

def is_amicable_pair(a, b, n_to_sum):
	return (a != b) & (n_to_sum[a] == b) & (n_to_sum[b] == a)

def sum_of_all_amicable_numbers(n):
	result = 0
	n_to_sum, dict_of_sums = get_dict_of_proper_divisor_sums(n)
	for a in n_to_sum:
		if (n_to_sum[a] in n_to_sum):
			if (n_to_sum[a] in dict_of_sums) & (is_amicable_pair(a, n_to_sum[a], n_to_sum)):
				result += a
	return result


start = time.time()
answer = sum_of_all_amicable_numbers(10000)
end = time.time()

print(answer)
print("Seconds passed: " + str(end-start))