import time

class Date:
	def __init__(self,day,month,year):
		self.day = day
		self.month = month
		self.year = year

days_in_month = {
	0: 31,
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30
}

def is_leapyear(year):
	if year % 100 == 0 & year % 400 != 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False

def get_weekday(date):
	weekday = date.day
	print(date.day)

def main():
	sundays = 0
	days_passed_since_monday = 365 - 31
	for year in range(1901,2001):
		for month in range(12):
			days_passed_since_monday += days_in_month[month]
			print(year)
			print("    " + str(month))
			if (month == 2) & is_leapyear(year):
				days_passed_since_monday += 1
				print("LEAPYEAR")
			weekday = days_passed_since_monday % 7
			if weekday == 6:
				sundays += 1
	print(sundays)
			
if __name__ == "__main__":
	main()