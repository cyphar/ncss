#!/usr/bin/env python3
# Enter your code for "Pac Man (I)" here.

from collections import deque
import copy
maze = open("maze.txt").readlines()

board = {}
for y in enumerate(maze):
	y_grid = list(y[1].strip())
	for x in enumerate(y_grid):

		# Add entry
		if not board.get(x[1]):
			board[x[1]] = []

		# Append point
		board[x[1]] += [(x[0],y[0])]

# Size of grid (x, y)
size = (len(maze[0]), len(maze))

# Copy positions
next_board = {}
next_board["P"] = board.get("P", [])
next_board["G"] = []
next_board["#"] = board.get("#", [])
next_board["."] = board.get(".", [])

# Preffered Order (since stack, do it in reverse)
order = ["u", "l", "d", "r"]

def move(point, ind):
	next_point = {
		"u" : (point[0], point[1] - 1),
		"d" : (point[0], point[1] + 1),
		"l" : (point[0] - 1, point[1]),
		"r" : (point[0] + 1, point[1])
	}

	return next_point.get(ind, point)

def bfs_path(start, end, walls):
	todo = deque([[start]])
	current = todo[0]

	while len(todo):
		current = todo.popleft()

		if current[-1] == end:
			return current

		for direction in order:
			new = current[:]
			point = move(new[-1], direction)

			if point in walls or point in new or new[-1] == end:
				continue

			new.append(point)
			todo.append(new)

	return [[start]]

# Update ghosts
for ghost in board.get("G", []):
	pacman = next_board["P"][0]
	walls = next_board["#"]

	best = bfs_path(ghost, pacman, walls)
	go = best[1:2]

	if go:
		next_board["G"] += [go[0]]
	else:
		next_board["G"] += [ghost]

# Generate next frame
next_frame = [[" " for x in range(size[0])] for y in range(size[1])]

for val in [".", "P", "G", "#"]:
	for point in next_board[val]:
		x = point[0]
		y = point[1]
		next_frame[y][x] = val

# Print frame
for line in next_frame:
	print("".join(line).strip())
