def collatz_sequence(n, sequence_length=0):
	while n != 1:
		if n & 1:
			n = 3*n+1
			sequence_length += 1	
		else:
			n = n//2
			sequence_length += 1
	return sequence_length+1

longest_sequence = 0
greatest_n = 0 
for n in range(1,1000000):
	current_sequence = collatz_sequence(n)
	if current_sequence > longest_sequence:
		longest_sequence = current_sequence
		greatest_n = n

print(longest_sequence)
print(greatest_n)