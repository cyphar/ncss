#!/usr/bin/env python2

l = [float(n) for n in iter(lambda:raw_input("Enter Number: "), "")]

print "Size: %d" % len(l)
print "Sum: %d" % sum(l)
print "Average:", (sum(l) / len(l))
print "Smallest: %d" % min(l)
print "Largest: %d" % max(l)
