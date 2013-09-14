#!/usr/bin/env python2

data = str(open("trains.txt", "rU").read()).split("\n")[:-1]
l = []
for x in data:
	l.append(x.lower())
s = str(raw_input("What is the current station? ")).lower()
if l.index(s) != len(l)-1:
	print "Next stop:",data[l.index(s)+1]
else:
	print "All out, all change!"
