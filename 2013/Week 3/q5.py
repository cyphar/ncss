#!/usr/bin/env python3
# Enter your code for "Unmasked! (II)" here.

import re
import string
from math import sqrt

def sim(a, b):
	top = sum(a[i] * b[i] for i in range(len(a)))
	bottom = sqrt(sum(x**2 for x in a)) * sqrt(sum(y**2 for y in b))
	return top / bottom

files = [name.strip() for name in open("texts.txt") if name.strip()]
stats = {}

biggest_word = 0

for name in files + ["unknown.txt"]:
	f = open(name).read()
	for word in f.split():
		word = word.strip(string.punctuation)
		if len(word) > biggest_word:
			biggest_word = len(word)

for name in files:
	stats[name] = [0] * biggest_word
	f = open(name).read()
	for word in f.split():
		word = word.strip(string.punctuation)
		if word:
			stats[name][len(word) - 1] += 1

unknown = [0] * biggest_word
f = open("unknown.txt").read()
for word in f.split():
	word = word.strip(string.punctuation)
	if word:
		unknown[len(word) - 1] += 1

comp = []

for f in stats:
	comp.append([sim(unknown, stats[f]), f])

for stat in sorted(comp)[::-1]:
	print("%.3f %s" % (stat[0], stat[1]))
