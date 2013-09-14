#!/usr/bin/env python2

names = open('names.txt', 'rU').read().split("\n")[:-1]
l = []
for n in names:
    if l.count(n) < 1:
        l.append(n)
for x in l:
    print x.rjust(9)+": "+"*"*names.count(x)
