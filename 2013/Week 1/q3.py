#!/usr/bin/env python3
# Enter your code for "Chuck A Word 180" here.

inp = []

while True:
	tmp = input("Line: ")
	if not tmp:
		break
	inp.append(tmp)

l = []

for line in inp:
	flipped = []

	for word in line.split(" "):
		flipped.append(word[::-1])

	l.append(" ".join(flipped))

for line in l:
	print(line)
