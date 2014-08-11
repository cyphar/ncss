#!/usr/bin/env python3
# Enter your code for "Mysterious Dates" here.

# THIS WAS MY INITAL SOLUTION.
# IT DOES NOT PASS THE TEST CASES.
# However, the reason I added this is because this code will take any date
# format (not just the given ones) and brute-force the first non-ambiguous
# representation. It is (in my opinion) a more "complete" solution.

import re
import itertools

PATTERN = r"(\d+).(\d+).(\d+)"

MONTHS = {
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
	11: 30,
	12: 31,
}

DAY = 0
MONTH = 1
YEAR = 2

def is_month(part):
	return 0 < part <= 12

def is_day(part, month):
	return 12 < part <= MONTHS[month]

def is_year(part, month):
	return MONTHS[month] < part <= 9999

def brute_force_order(date):
	for fmt in itertools.permutations([DAY, MONTH, YEAR], 3):
		fmt = list(fmt)

		day = date[fmt.index(DAY)]
		month = date[fmt.index(MONTH)]
		year = date[fmt.index(YEAR)]

		if not is_month(month) or not is_day(day, month) or not is_year(year, month):
			continue

		return [fmt.index(DAY), fmt.index(MONTH), fmt.index(YEAR)]

	return None

def ambiguity_order(dates):
	for date in dates:
		order = brute_force_order(date)

		if order:
			break
	else:
		return None

	fmt = {
		"day": order[DAY],
		"month": order[MONTH],
		"year": order[YEAR],
	}

	return fmt

def main():
	with open("ambiguous-dates.txt") as f:
		data = f.read()
		dates = re.findall(PATTERN, data)

	if not dates:
		return

	dates = [tuple(int(p) for p in d) for d in dates]
	order = ambiguity_order(dates)

	# No order found.
	if not order:
		print("No unambiguous dates found")
		return

	for date in dates:
		day = date[order["day"]]
		month = date[order["month"]]
		year = date[order["year"]]

		print("%.4d-%.2d-%.2d" % (year, month, day))

if __name__ == "__main__":
	main()
