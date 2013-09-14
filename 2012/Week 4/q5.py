#!/usr/bin/env python2

import random
words = str(open("words.txt", "rU").read()).split("\n")[:-1]
many = int(raw_input("How many questions (more is better)? "))
rand = random.sample(words,many)
yes = 0.0
for i in rand:
	if len(i) > 9:
		print "Wow, this is a long one!"
	y = raw_input("Do you know '"+i+"'? ")
	if y == "yes" or y == "y":
		yes += 1.0

print "Out of the",len(words),"words in my list, I estimate that you know",int(yes/many*len(words)),"of them."
