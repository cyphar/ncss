#!/usr/bin/env python3
# Enter your code for "Typo finder" here.

import re

def main():
	words = []
	for line in iter(input, ""):
		line = line.strip()
		words += [word.lower() for word in re.findall(r"\b\w+\b", line) if len(word) >= 4]

	commons = {}
	for word in words:
		common = re.sub(r"[aeiou]", "", word)

		if common not in commons:
			commons[common] = set()

		commons[common].add(word)

	flat = [words for _, words in commons.items() if len(words) > 1]
	for words in flat:
		print(*[word.lower() for word in sorted(words)])

if __name__ == "__main__":
	main()
