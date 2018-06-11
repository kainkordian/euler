import time

def sum_on_diagonals(square_maximum):
	new_ring_counter = 0
	sum_on_diagonals = 0
	step_size = 2
	i = 1
	while i <= square_maximum:
		if new_ring_counter == 4:
			new_ring_counter = 0
			step_size += 2
		new_ring_counter += 1
		sum_on_diagonals += i
		i += step_size
	return sum_on_diagonals


def main(argv=None):
	print(sum_on_diagonals(argv*argv))
	
if __name__ == "__main__":
	main()