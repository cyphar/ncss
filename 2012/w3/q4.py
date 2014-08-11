#!/usr/bin/env python2

w = raw_input("Enter words: ")
f,l = w.split()

sa = False

if f[0] == l[0] and f[-1] == l[-1]:
	if sorted(f[1:-1]) == sorted(l[1:-1]):
		sa = True

if sa:
	print "Super Anagram!"
else:
	print "Huh?"
