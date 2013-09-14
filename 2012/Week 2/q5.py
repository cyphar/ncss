#!/usr/bin/env python2

num = int(raw_input("Enter a row number: "))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if num % 26 != 0:
    print alpha[num % 26 - 1] * (num / 26 + 1)
else:
    print alpha[num % 26 - 1] * (num / 26)
