#!/usr/bin/env python3
# Enter your code for "Kaprekar Numbers" here.

def is_kaprekar(num):
	if num == 1:
		return True

	sqr = str(num ** 2)
	combs = [(sqr[:mid], sqr[mid:]) for mid in range(1, len(sqr))]

	for left, right in combs:
		left = int(left)
		right = int(right)

		if not left or not right:
			continue

		if left + right == num:
			return True

	return False
