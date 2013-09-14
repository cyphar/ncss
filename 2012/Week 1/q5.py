#!/usr/bin/env python2

polly = raw_input("Polly: ")
if(int(len(polly)) % 10 == 0):
	num_crackers = int(len(polly) / 10)
else:
	num_crackers = int((len(polly) / 10)+1)
if polly == '':
	print " "
else:
	print "CRACKER " * num_crackers
