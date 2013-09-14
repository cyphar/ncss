#!/usr/bin/env python2

t = []
m = []
b = []
for x in range(3):
	t.append(int(raw_input("Enter Number: ")))
for x in range(3):
	m.append(int(raw_input("Enter Number: ")))
for x in range(3):
	b.append(int(raw_input("Enter Number: ")))

if sum(t) == 15 and sum(m) == 15 and sum(b) == 15 and t[0]+m[0]+b[0] == 15 and t[1]+m[1]+b[1] == 15 and t[2]+m[2]+b[2] == 15 and t[0]+m[1]+b[2] == 15 and t[2]+m[1]+b[0] == 15:
	print "Valid!"
else:
	print "Invalid!"
