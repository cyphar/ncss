#!/usr/bin/env python3
# Enter your code for "Mysterious Dates" here.

# This is my *legit* solution.
# If you want a solution that does ... more, look at q4complex.py.

import re

PATTERN = r"(\d+)[^A-Za-z0-9](\d+)[^A-Za-z0-9](\d+)"

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

FORMATS = [
	(DAY, MONTH, YEAR),
	(MONTH, DAY, YEAR),
	(YEAR, MONTH, DAY),
]

def is_month(part):
	return 0 < part <= 12

def is_day(part, month):
	return 0 < part <= MONTHS[month]

def is_year(part):
	return 0 < part <= 9999

def matching_orders(date):
	matching = []

	for fmt in FORMATS:
		day = date[fmt.index(DAY)]
		month = date[fmt.index(MONTH)]
		year = date[fmt.index(YEAR)]

		if not is_month(month) or not is_day(day, month) or not is_year(year):
			continue

		matching.append((fmt.index(DAY), fmt.index(MONTH), fmt.index(YEAR)))

	return matching

def ambiguity_order(dates):
	for date in dates:
		orders = matching_orders(date)

		if len(orders) == 1:
			break
	else:
		return None

	order = orders[0]
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
