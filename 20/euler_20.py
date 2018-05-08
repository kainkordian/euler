def factorial(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result
# print(factorial(4))
print(sum(map(lambda x: int(x), list(str(factorial(100))))))