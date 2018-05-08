import time

def main(argv=None):
	start = time.time()
	distinct_terms = len(set(a**b for a in range(2, argv+1) for b in range(2, argv+1)))
	end = time.time()
	print("Seconds passed: " + str(end - start))
	return distinct_terms

if __name__ == "__main__":
	main(100)