#!/usr/bin/env python2

bpj = raw_input("Bytes per joule: ")
if bpj != '':
	bpt = int(bpj) * 62000 		#Bytes per cup of tea
	tpb = bpt**-1			#Cups of tea per byte
	tptb = tpb * 10**12		#Cups of tea per terrabyte
	print str(tptb) + " cups of tea per terabyte"
