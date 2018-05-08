sum_of_squares = sum(map(lambda x: x**2, range(101)))
square_of_sum = sum(range(101))**2
print(abs(square_of_sum - sum_of_squares))