#!/usr/bin/env python2

l = {}
names = []

for n in open('names.txt', 'rU'):
	n = n.strip()
	if n not in l:
		l[n] = 0
	l[n] += 1

	if n not in names:
		names.append(n)

for x in names:
    print x.rjust(9) + ":", "*" * l[x]
