#!/usr/bin/env python2

words = [k.strip() for k in open('dictionary.txt', 'rU')]

d = {}
for x in words:
	a,b = x.split(",")
	d[a] = b

for inp in iter(lambda:raw_input("English: "), ""):
	abo = [d[s] for s in inp.split()]
	print " ".join(abo)
