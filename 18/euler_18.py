import time

def get_triangle():
	data = open("data.txt", "r")
	triangle = []
	for row in data:
		triangle.append(list(map(lambda x: int(x), row.split(" "))))
	return triangle

def find_maximum_total(triangle):
	for row in range(len(triangle)-1,0,-1):
		for double in range(len(triangle[row])-1):
			triangle[row-1][double] += max(triangle[row][double], triangle[row][double+1])
	return triangle[0][0]

test_triangle = [[3], [7,4], [2,4,6], [8,5,9,3]]
triangle = get_triangle()
print(find_maximum_total(triangle))