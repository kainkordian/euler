import time


# If the remainder down the division streak repeats, the whole diviosn cycle from the last time this remainder occurred will repeat.
# Obviously -.-
def recurrent_cycle_length(n,d):
	remainder_list = []
	remainder = 1
	while remainder:
		remainder = n % d
		if remainder in remainder_list:
			return (len(remainder_list) - remainder_list.index(remainder))
		remainder_list.append(remainder)
		n = (n * 10) % d
	return 0

longest_cycle = 0
d_with_longest_cycle = 0
for d in range(1,1000):
	cycle_length = recurrent_cycle_length(1,d)
	if cycle_length > longest_cycle:
		longest_cycle = cycle_length
		d_with_longest_cycle = d

print("D with longest cycle: " + str(d_with_longest_cycle))
print("Longest cycle length: " + str(longest_cycle))