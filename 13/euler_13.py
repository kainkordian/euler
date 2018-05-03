digits_file = open("digits.txt", "r")
numbers = []
for number in digits_file:
	numbers.append(int(number))

sum_of_numbers = sum(numbers)
print(str(sum_of_numbers)[:10])