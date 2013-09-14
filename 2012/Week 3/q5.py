#!/usr/bin/env python2

names = []
f = []
l = []
while True:
	name = raw_input("Enter classmate: ")
	if name == '':
		break
	names.append(name)
for each in names:
	f.append(each.split()[0]) #first names
	l.append(each.split()[1]) #last names
for x in range(len(f)):
	for y in range(len(l)):
		print f[x],l[y]
