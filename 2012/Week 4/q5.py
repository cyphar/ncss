#!/usr/bin/env python2

import random

words = [k.strip() for k in open("words.txt", "rU")]
many = int(raw_input("How many questions (more is better)? "))
rand = random.sample(words,many)

yes = 0
for i in rand:
	if len(i) > 9:
		print "Wow, this is a long one!"

	y = raw_input("Do you know '"+i+"'? ")
	if y in ["yes", "y"]:
		yes += 1

print "Out of the %d words in my list, I estimate that you know %d of them." % (len(words), float(yes)/many * len(words))
