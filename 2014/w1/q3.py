#!/usr/bin/env python3
# Enter your code for "Cellular automata" here.

num = int(input())
rows = [input()]

i = 1
while i < num:
	prev = rows[i-1]
	new = ["."] * len(prev)

	for j, _ in enumerate(prev):
		left = (j - 1) % len(prev)
		right = (j + 1) % len(prev)

		if (prev[left] == "*") ^ (prev[right] == "*"):
			new[j] = "*"

	rows.append("".join(new))
	i += 1

if num > 0:
	for row in rows:
		print(row)
