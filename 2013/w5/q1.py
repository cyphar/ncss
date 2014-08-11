#!/usr/bin/env python3
# Enter your code for "Patches of Paint" here.

ground = open("patches.txt").readlines()

cache = set()
for y in enumerate(ground):
	y_grid = list(y[1].strip())
	for x in enumerate(y_grid):
		point = (x[0], y[0])

		if x[1] == "%":
			cache.add(point)

move = [
	lambda p:(p[0], p[1] - 1), # up
	lambda p:(p[0], p[1] + 1), # down
	lambda p:(p[0] - 1, p[1]), # left
	lambda p:(p[0] + 1, p[1]), # right
	lambda p:(p[0] - 1, p[1] - 1), # up left
	lambda p:(p[0] + 1, p[1] - 1), # up right
	lambda p:(p[0] - 1, p[1] + 1), # down left
	lambda p:(p[0] + 1, p[1] + 1)  # down right
]

# Basic Flood Fill
def paint_trail(start):
	Q = [start]
	out = []

	while Q:
		n = Q.pop()
		if n in cache:
			cache.remove(n)
			out += [n]

			for m in [k(n) for k in move]:
				if m in cache:
					Q += [m]

	return out

splotches = 0
while cache:
	get = list(cache)[0]
	path = paint_trail(get)
	splotches += 1

print("%d patch%s" % (splotches, "es" if splotches != 1 else ""))
