#!/usr/bin/env python2

input = raw_input("Enter a sequence: ")

inp = str(input)
seq = input.upper()
l = len(seq)

#if seq.isdigit:
#    print "This is not a protein."

if (l % 3) != 0:
    print "This is not a protein."

elif seq.count("AUG", 0, 3) != 1:
    print "This is not a protein."

elif seq.count("UAA", l - 3, l) != 1 and seq.count("UAG", l - 3, l) != 1 and seq.count("UGA", l - 3, l) != 1:
    print "This is not a protein."

else:
    print "This is a possible protein."
