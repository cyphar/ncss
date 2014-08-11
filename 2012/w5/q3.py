#!/usr/bin/env python2

inp = list(iter(lambda:raw_input("Row: "), ""))
grid = {}
for y in enumerate(inp):
	for x in enumerate(y[1]):
		grid[x[1]] = (x[0], y[0])

def snake():
	if "@" not in grid or "p" not in grid:
		return ["error"]

	apple = grid["@"]
	person = grid["p"]

	out = []

	if apple[1] > person[1]:
		out += ["down"]
	elif apple[1] < person[1]:
		out += ["up"]

	if apple[0] > person[0]:
		out += ["right"]
	elif apple[0] < person[0]:
		out += ["left"]

	return out

print "\n".join(snake())
