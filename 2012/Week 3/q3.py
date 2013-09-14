#!/usr/bin/env python2

num = int(raw_input("How many steps? "))
i = 2

print "__" #first line

while i < 2 * num:
	print " " * (i) + "|_"
	i += 2

print "_" *(2 *(num))+"|"  #final line
