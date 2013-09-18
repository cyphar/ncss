#!/usr/bin/env python2

num = int(raw_input("How many steps? "))
i = 2

print "__"

for i in range(1, 2 * num, 2)[:-1]:
	print " " * (i+1) + "|_"

print "__" * num + "|"
