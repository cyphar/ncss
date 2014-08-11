#!/usr/bin/env python3
# Enter your code for "SMS T9 Texting" here.

import re

KEYPAD = {v: i+2 for i, V in enumerate("abc def ghi jkl mno pqrs tuv wxyz".split()) for v in V}
LOOKUP = {i+2: v[0] for i, v in enumerate("abc def ghi jkl mno pqrs tuv wxyz".split())}

def generate_freqs(entries):
	freqs = {}

	for entry in entries:
		word, freq = entry.split()

		keys = tuple(KEYPAD[i] for i in word)

		if keys not in freqs:
			freqs[keys] = []

		freqs[keys].append((word, int(freq)))
		freqs[keys] = sorted(freqs[keys], key=lambda n: -n[1])

	return freqs

def main():
	with open("frequencies.txt") as f:
		entries = [line.strip() for line in f if line.strip()]
		freqs = generate_freqs(entries)

	words = []
	for seq in input().split():
		keys, num = re.match(r"(\d+)(\**)", seq).groups()
		keys = tuple(map(int, keys))

		if keys not in freqs:
			word = "".join(LOOKUP[key] for key in keys)
			words.append(word)
			continue

		possibles = freqs[keys]
		word = possibles[len(num) % len(possibles)]
		words.append(word[0])

	print(*words)

if __name__ == "__main__":
	main()
