#!/usr/bin/env python2

i = int(raw_input("How many random numbers do you want? "))
seed = int(raw_input("Seed? "))

for x in range(i):
    seed = (seed * 13) % 97
    print seed
