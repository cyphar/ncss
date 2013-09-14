#!/usr/bin/env python3
# Enter your code for "You, Me And The TLA" here.

lines = 0
tlas = 0

import re
for line in open("sentences.txt"):
	lines += 1
	if re.search("(?:[^A-Z]|\A)+[A-Z]{3}(?:[^A-Z]+|\Z)", line) != None:
		tlas += 1

print("%.1f%% of sentences contain a TLA" % ((tlas / lines) * 100))

