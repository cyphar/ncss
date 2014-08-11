#!/usr/bin/env python2

bpj = int(raw_input("Bytes per joule: "))
if bpj != '':
	amount = 1.0 / (int(bpj) * 62000) * 1e12
	print "%s cups of tea per terabyte" % str(amount)
