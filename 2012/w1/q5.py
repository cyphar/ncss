#!/usr/bin/env python2

import math

polly = raw_input("Polly: ")
num_crackers = math.ceil(len(polly) / 10.0)

if not polly:
	print " "
else:
	print "CRACKER " * int(num_crackers)
