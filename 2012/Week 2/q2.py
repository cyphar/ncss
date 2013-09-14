#!/usr/bin/env python2

i = raw_input("How many random numbers do you want? ")
seed = int(raw_input("Seed? "))

for x in range(0,int(i)):
    seed = (seed * 13) % 97
    print seed
