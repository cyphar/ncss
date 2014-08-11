#!/usr/bin/env python3
# Enter your code for "Triple-Double-Letter" here.

import re

matches = []
words = open("words.txt").readlines()

for word in words:
	if len(set(re.findall(r"(\w)\1", word))) >= 3:
		matches.append(word.strip())

for match in sorted(matches):
	print(match)
