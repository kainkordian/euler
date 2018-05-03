triangle_numbers = {}
current_triangle_number = 0
for i in range(1,21):
	current_triangle_number += i
	triangle_numbers[i] = current_triangle_number

def sum_until(n, f):
	result = 0
	for i in range(1,n+1):
		result += f(i)
	return result

to_3x3 = sum_until(3+1, lambda x: triangle_numbers[x])


to_4x4 = sum_until(4+1, (lambda x: sum_until(x, \
						(lambda x: sum_until(x, lambda x: x)))))

to_20x20 = sum_until(20+1, (lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: sum_until(x, \
						(lambda x: triangle_numbers[x]))))))))))))))))))))))))))))))))))))

# to_20x20 = sum_until(20+1, (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, \
# 						   (lambda x: sum_until(x, lambda x: x)))))))))))))))))))))))))))))))))))))

print(to_20x20)