#!/usr/bin/env python3
# Enter your code for "Nth Caesar Shift" here.

def caesar_shift(msg, n):
	cipher = ""
	alpha = ord("z") - ord("a") + 1
	n -= 1

	for letter in msg:
		new = letter
		if letter.isupper():
			new = chr((ord(letter) + n - ord("Z")) % alpha + ord("A"))
		elif letter.islower():
			new = chr((ord(letter) + n - ord("z")) % alpha + ord("a"))
		cipher += new
	return cipher
