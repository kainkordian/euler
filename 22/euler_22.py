import time

def get_alphabetical_value(name):
	result = 0
	for character in list(name):
		result += ord(character)-64
	return result

def get_names():
	return next(open("data.txt", "r")).replace("\"","").split(",")

start = time.time()

names = get_names()
names = sorted(names)
total_name_score = 0
for name_position in range(len(names)):
	total_name_score += (name_position+1) * get_alphabetical_value(names[name_position])
end = time.time()

print("Seconds passed: " + str(end-start))
print(total_name_score)