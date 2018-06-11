import time

digit_limit = 1000

a = 1
b = 1

index = 1

start = time.time()
while True:
	if len(str(a)) == digit_limit:
		break
	temp = b
	b = b + a
	a = temp
	index += 1
end = time.time()

print("Sendonds passed :" + str(end - start))
print(index)
print(a)
