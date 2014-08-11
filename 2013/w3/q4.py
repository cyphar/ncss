#!/usr/bin/env python3
# Enter your code for "Calculator Printer" here.

number = input("Number: ")
width = int(input("Width: "))


digits = { "0" : [1, 1, 1, 0, 1, 1, 1],
	   "1" : [0, 0, 1, 0, 0, 1, 0],
	   "2" : [1, 0, 1, 1, 1, 0, 1],
	   "3" : [1, 0, 1, 1, 0, 1, 1],
	   "4" : [0, 1, 1, 1, 0, 1, 0],
	   "5" : [1, 1, 0, 1, 0, 1, 1],
	   "6" : [1, 1, 0, 1, 1, 1, 1],
	   "7" : [1, 0, 1, 0, 0, 1, 0],
	   "8" : [1, 1, 1, 1, 1, 1, 1],
	   "9" : [1, 1, 1, 1, 0, 1, 1]
}

final = []

for digit in number:
	final.append([])
	for bar in digits[digit]:
		final[-1].append(bar)

final = list(zip(*final))

for i in range(5):
	if not i % 2:
		# Horizontal Bars
		line = []
		for num in final[i + (i + 1)//2]:
			line.append(" " + " -"[num] * width + " ")
		print(*line)
	else:
		# Vertical Bars
		ind = i + (i + 1)//2 - 1
		now = list(zip(*final[ind:ind+2]))

		for line in range(width):
			l = []
			for num in now:
				l.append(" |"[num[0]] + " " * width + " |"[num[1]])
			print(*l)
