MAX = 4000000
swapper = 2
a = 1
b = 2
sum_of_even_fibonaccis = 0

while True:
	temp = b
	b = a + b
	a = temp
	swapper += 1
	if a >= MAX:
		break
	if swapper == 3:
		print("Even: " + str(a))
		sum_of_even_fibonaccis += a
		swapper = 0
	else:
		print("Odd: " + str(a))

print(sum_of_even_fibonaccis)
