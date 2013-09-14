#!/usr/bin/env python2

num = raw_input("How many characters did you write? ")
if int(num) <= 140:
	print "That belongs on Twitter."
if int(num) > 140 and int(num) < 5000:
	print "That belongs on Facebook."
if int(num) >= 5000:
	print "That belongs on your blog."
