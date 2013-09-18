#!/usr/bin/env python2

number1 = raw_input("Enter a four digit number, using at least two different digits: ")
number = int(number1)
i = 0
while number not in [0, 6174]:
	i += 1
	number = str(number).zfill(4)
	a = "".join(sorted(number))
	d = a[::-1]

	number = abs(int(a) - int(d))
	if int(a) < int(d):
		print "%s - %s = %s" % (d, a, str(number).zfill(4))
	else:
		print "%s - %s = %s" % (a, d, str(number).zfill(4))

print str(number1).zfill(4), "took", i, "iteration(s)."
