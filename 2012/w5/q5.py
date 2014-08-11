#!/usr/bin/env python2

def code(col, msg):
	possible = []
	for person in col:
		worked = True
		if len(person) > len(msg):
			worked = False
		else:
			for char in enumerate(person): #each char
				if char[1] not in msg[char[0]]:
					worked = False
					break
		if worked:
			possible += [person]
	return possible

col = raw_input("Who are your collegues? ").split()
msg = raw_input("What is the message? ").split()

for x in code(col, msg):
	print x,"could have written this."
