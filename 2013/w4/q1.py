#!/usr/bin/env python3
# Enter your code for "Carry On" here.

def carries(a, b):
	biglen = max([len(str(a)), len(str(b))]) + 1
	x,y = str(a).zfill(biglen),str(b).zfill(biglen)

	new = []
	carries = 0
	for digit in zip(x, y):
		new += [[digit[0], digit[1], 0]]

	for pos in range(biglen - 1, -1, -1):
		place = new[pos]
		carry = int(place[0]) + int(place[1]) + place[2] >= 10

		if 0 < pos - 1 < len(new):
			new[pos - 1][2] += carry

		carries += carry

	return carries

if __name__ == "__main__":
	print(carries(123, 1))
	print(carries(199, 1))
	print(carries(189, 1))
	print(carries(1094, 3167))
	print(carries(999, 1))
