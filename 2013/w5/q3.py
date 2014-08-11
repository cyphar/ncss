#!/usr/bin/env python3
# Enter your code for "Pac Man (II)" here.

from collections import deque
import copy
maze = open("maze.txt").readlines()

board = {}
walls = set()
for y in enumerate(maze):
	y_grid = list(y[1].strip())
	for x in enumerate(y_grid):

		# Add entry
		if not board.get(x[1]):
			board[x[1]] = []

		point = (x[0], y[0])

		# Append point
		board[x[1]] += [point]

		if x[1] == "#":
			walls.add(point)

# Size of grid (x, y)
size = (len(maze[0]), len(maze))

# Preffered Order
order = ["U", "L", "D", "R"]

def move(point, ind):
	next_point = {
		"U" : (point[0], point[1] - 1),
		"D" : (point[0], point[1] + 1),
		"L" : (point[0] - 1, point[1]),
		"R" : (point[0] + 1, point[1])
	}

	return next_point.get(ind, point)

def reconstruct(came_from, point):
	if point in came_from:
		return reconstruct(came_from, came_from[point]) + [point]
	else:
		return [point]

def bfs_path(start, end, walls):
	todo = deque([start])
	came_from = {}
	seen = set([start])

	while todo:
		current = todo.popleft()

		if current == end:
			return reconstruct(came_from, current)

		for direction in order:
			point = move(current, direction)

			if point in walls or point in seen:
				continue

			seen.add(point)
			came_from[point] = current
			todo.append(point)

	return [[start]]

# Copy positions
next_board = {}
next_board["P"] = board.get("P", [(0, 0)])
next_board["G"] = board.get("G", [])
next_board["#"] = board.get("#", [])
next_board["."] = board.get(".", [])

RUNNING = 1
WIN = 2
LOSS = 3

state = RUNNING
new_score = score = 0
commands = input("Commands: ").split()

for command in commands:
	if not next_board["."]:
		state = WIN
		break

	# Generate next frame
	if command == "O":
		next_frame = [[" " for x in range(size[0])] for y in range(size[1])]

		for val in [".", "P", "G", "#"]:
			for point in board.get(val, []):
				x = point[0]
				y = point[1]
				next_frame[y][x] = val
		# Print frame
		print("Points: %d" % (score))
		for line in next_frame:
			print("".join(line).strip())

		continue

	# Update Pacman
	if command in order:
		tmp = move(board["P"][0], command)

		if tmp not in next_board["#"]:
			next_board["P"] = [tmp]

			if next_board["P"][0] in next_board["."]:
				next_board["."].remove(next_board["P"][0])
				new_score += 1
		else:
			next_board["P"] = board["P"][:]

	# Update ghosts
	next_board["G"] = []
	for ghost in board.get("G", []):
		pacman = board["P"][0]

		best = bfs_path(ghost, pacman, walls)
		go = best[1:]

		if go:
			next_board["G"] += [go[0]]
		else:
			next_board["G"] += [ghost]

	# Check end state
	if not next_board["."]:
		score = new_score
		state = WIN
		break

	if next_board["P"][0] in next_board["G"]:
		score = new_score
		state = LOSS
		break

	if next_board["P"][0] in board.get("G", []):
		# Set pacman and pills back
		next_board["P"] = [board["P"][0]]
		next_board["."] = board.get(".", [])
		state = LOSS
		break

	score = new_score

	board = {}
	for k in next_board:
		board[k] = next_board[k][:]

if state == RUNNING and not board.get(".", []):
	state = WIN

if state == WIN:
	print("You won!")
elif state == LOSS:
	print("You died!")

# Generate next frame
next_frame = [[" " for x in range(size[0])] for y in range(size[1])]

for val in [".", "P", "G", "#"]:
	for point in next_board.get(val, []):
		x = point[0]
		y = point[1]
		next_frame[y][x] = val

# Print frame
print("Points: %d" % (score))
for line in next_frame:
	print("".join(line).strip())
