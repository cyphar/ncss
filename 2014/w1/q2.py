#!/usr/bin/env python3
# Enter your code for "Clap The Beat" here.

divisions = int(input())
divisors = []
for _ in range(divisions):
	divisor = int(input())
	divisors.append(divisor)

beats = int(input())
length = len("%d" % beats)

for beat in range(beats):
	beat += 1
	line = ("%d:" % beat).rjust(length + 1)

	for divisor in divisors:
		if beat % divisor:
			line += " "
		else:
			line += "X"

	line = line.rstrip()
	print(line)
