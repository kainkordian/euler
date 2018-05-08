import time

def main(argv=None):
	start = time.time()
	sum_of_magic_numbers = 0
	left_hand_side_str = ""
	for a in range(4):
		left_hand_side_str += str(a)
		for b in range(10):
			left_hand_side_str += str(b)
			for c in range(10):
				left_hand_side_str += str(c)
				for d in range(10):
					left_hand_side_str += str(d)
					for e in range(10):
						left_hand_side_str += str(e)
						for f in range(10):
							left_hand_side_str += str(f)
							right_hand_side = sum(map(lambda x: x**argv, [a,b,c,d,e,f]))
							left_hand_side = int(left_hand_side_str)
							if (left_hand_side == right_hand_side) & (left_hand_side > 1):
								print(left_hand_side)
								sum_of_magic_numbers += left_hand_side
							left_hand_side_str = left_hand_side_str[:-1]
						left_hand_side_str = left_hand_side_str[:-1]
					left_hand_side_str = left_hand_side_str[:-1]
				left_hand_side_str = left_hand_side_str[:-1]
			left_hand_side_str = left_hand_side_str[:-1]
		left_hand_side_str = left_hand_side_str[:-1]
	end = time.time()
	print("Seconds passed: " + str(end - start))
	return sum_of_magic_numbers

if __name__ == "__main__":
	main()