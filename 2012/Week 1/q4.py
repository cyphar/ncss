#!/usr/bin/env python2

num = int(raw_input("How many characters did you write? "))
if num <= 140:
	print "That belongs on Twitter."
elif num < 5000:
	print "That belongs on Facebook."
else:
	print "That belongs on your blog."
