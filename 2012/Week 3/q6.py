#!/usr/bin/env python2

number1 = raw_input("Enter a four digit number, using at least two different digits: ")
if number1.isdigit() == True:
	number = int(number1)
	i = 0
	while number != 6174 and number != 0:
		i += 1
		number = str(number).zfill(4)
		d = "".join(sorted(str(number), reverse=True))
		a = "".join(sorted(str(number)))
		if int(a) < int(d):
			number = int(d) - int(a)
			print d+" - "+a+" = "+str(number).zfill(4)
		else:
			number = int(a) - int(d)
			print a+" - "+d+" = "+str(number).zfill(4)
	print str(number1).zfill(4)+" took "+str(i)+" iteration(s)."
