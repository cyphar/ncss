#!/usr/bin/env python2

def spoon(s,a,b):
	a_ = a
	b_ = b
	for x in ["a","e","i","o","u"]:
		if x in a:
			if len(a[:a.index(x)]) < len(a_):
				a_ = a[:a.index(x)]
		if x in b:
			if len(b[:b.index(x)]) < len(b_):
				b_ = b[:b.index(x)]
	_a = a.replace(a_,b_)
	_b = b.replace(b_,a_)
	s = s.split()
	s[s.index(a)] = _a
	s[s.index(b)] = _b
	return ' '.join(s)
orig = str(raw_input("Enter sentence: "))
fir = str(raw_input("Enter word 1: "))
sec = str(raw_input("Enter word 2: "))
print spoon(orig,fir,sec)
