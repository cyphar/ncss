#!/usr/bin/env python2

names = zip(*[name.split() for name in iter(raw_input, "")])

if names:
	for first in names[0]:
		for last in names[1]:
			print first, last
