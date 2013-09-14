#!/usr/bin/env python2

l = list()
while True:
	x = raw_input("Enter Number: ")
	if x == '':
		break
	l.append(float(x))

length = int(len(l))
added = int(sum(l))
average = float(sum(l)) / len(l)
minimum = int(min(l))
maximum = int(max(l))

print "Size:", length
print "Sum:", added
print "Average:", average
print "Smallest:", minimum
print "Largest:", maximum
