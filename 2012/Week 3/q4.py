#!/usr/bin/env python2

w = raw_input("Enter words: ")
f = list(w.split()[0])
l = list(w.split()[1])
sa = False
if f != l:
	if f.pop(0) != l.pop(0) or f.pop(len(f)-1) != l.pop(len(l)-1):
		sa = False
	else:
		f.sort()
		l.sort()
		if f == l:
			sa = True
		else:
			sa = False
else:
	sa = True

if sa == True:
	print "Super Anagram!"
else:
	print "Huh?"
