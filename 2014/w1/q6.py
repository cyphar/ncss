#!/usr/bin/env python3
# Enter your code for "1800-BUY-NOW" here.

def count_collisions(text, keypad):
	occur = {}
	for word in text.split():
		keys = tuple(keypad[letter] for letter in word.lower())

		if keys not in occur:
			occur[keys] = 0
		occur[keys] += 1

	return sum(val for val in occur.values() if val > 1)
