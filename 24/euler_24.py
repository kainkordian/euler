import time
import itertools
def permute(l):
	permutations = []
	if l == []:
		return ""
	if len(l) == 1:
		return [l]
	for i in range(len(l)):
		sub_lists = permute(l[:i] + l[i+1:])
		permutations += list(map(lambda x: [l[i]] + x, sub_lists))
	return permutations

digits = list(range(10))
test_digits = list(range(3))
start = time.time()
perms =  list(itertools.permutations(digits))
end = time.time()

millionth_permutation = perms[999999]
millionth_permutation = str(millionth_permutation).replace("[","").replace("]","").replace(" ","").replace(",","")
print("Seconds passed: " + str(end - start))
print(millionth_permutation)
print(len(perms))
print(perms[:10])
