#!/usr/bin/env python3
# Enter your code for "Vicinal Words" here.

VICINAL = 0
NONVICINAL = 1
OTHER = 2

def _ord(char):
	return ord(char) - ord('a')

def _chr(ordinal):
	return chr(ordinal + ord('a'))

def get_vicinal(word):
	vicinal = []

	word = word.lower()
	for letter in word:
		left = (_ord(letter) - 1) % 26
		right = (_ord(letter) + 1) % 26

		if _chr(left) in word or _chr(right) in word:
			vicinal.append(letter)

	if not vicinal:
		return NONVICINAL

	if len(vicinal) != len(word):
		return OTHER

	return VICINAL

def main():
	for line in iter(input, ""):
		vicinals = []
		nonvicinals = []

		words = line.strip().split()

		for word in words:
			typ = get_vicinal(word)

			if typ == VICINAL:
				vicinals.append(word)

			if typ == NONVICINAL:
				nonvicinals.append(word)

		if vicinals:
			print("Vicinals:", *vicinals)

		if nonvicinals:
			print("Non-vicinals:", *nonvicinals)

if __name__ == "__main__":
	main()
