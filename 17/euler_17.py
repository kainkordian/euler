spelled_numbers = {
	0: "",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety"
}

long_long_string = ""
for i in range(1,1001):
	if i in spelled_numbers:
		long_long_string += spelled_numbers[i]
	elif i == 1000:
		long_long_string += "onethousand"
	else:
		if i > 99:
			temp = i // 100
			long_long_string += spelled_numbers[temp] + "hundred"
			i = i - temp * 100
			if i > 0:
				long_long_string += "and"
		if i in spelled_numbers:
			long_long_string += spelled_numbers[i]
		else: 
			temp = (i // 10) * 10
			long_long_string += spelled_numbers[temp]
			i = i - temp
			long_long_string += spelled_numbers[i]

print(len(long_long_string))