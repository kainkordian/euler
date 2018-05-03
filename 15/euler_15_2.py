import time
import numpy as np

def paths_in_grid(n,m):
	knode_visits = np.ones((n+1,m+1))
	for i in range(1,n+1):
		for j in range(1,m+1):
			knode_visits[i,j] = knode_visits[i-1,j] + knode_visits[i,j-1]
	return knode_visits[n,m]

rows = int(input("Rows?: "))
columns = int(input("Columns?: "))
start = time.time()
print(int(paths_in_grid(rows,columns)))
end = time.time()
print("Seconds passed:")
print(end - start)