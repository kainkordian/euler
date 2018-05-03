multiples_of_3 = set(x*3 for x in range(1,334))
multiples_of_5 = set(x*5 for x in range(1,200))
print(sum(multiples_of_3 | multiples_of_5))