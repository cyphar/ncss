#!/usr/bin/env python2

import math

num = int(raw_input("Enter a row number: "))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print alpha[num % 26 - 1] * int(math.ceil(num / 26.0))
