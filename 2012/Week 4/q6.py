#!/usr/bin/env python2

words = open('dictionary.txt', 'rU').read().split("\n")[:-1]
d = {}
for x in words:
    a = x.split(",")[0]
    b = x.split(",")[1]
    d[a] = b
lawl = raw_input("English: ").split()
while lawl:
    abo = ""
    for s in lawl:
        abo += d[s] + " "
    print abo[:-1]
    lawl = raw_input("English: ").split()
