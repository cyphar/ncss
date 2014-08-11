#!/usr/bin/env python3
# Enter your code for "Counting Pythons" here.

import collections

def load_room(path):
	with open(path) as f:
		skins = set()
		head = None

		# Load a grid from a file.
		for y, line in enumerate(f):
			for x, cell in enumerate(line.strip()):
				if cell == "X":
					skins.add((x, y))
				elif cell in "<>^v":
					head = ((x, y), cell)

	return head, skins

def bfs(start, valids):
	if start not in valids:
		return set()

	seen = set([start])
	todo = collections.deque([start])

	# All possible movements.
	moves = [
		lambda p: (p[0] + 1, p[1]),
		lambda p: (p[0] - 1, p[1]),
		lambda p: (p[0], p[1] - 1),
		lambda p: (p[0], p[1] + 1),
	]

	# Exhaust all posibilities.
	while todo:
		current = todo.popleft()

		# Deal with bad start.
		if current not in valids:
			continue

		# Try every direction.
		for move in moves:
			point = move(current)

			# Not a skin.
			if point not in valids:
				continue

			# Already seen.
			if point in seen:
				continue

			# New point. Save it for later.
			seen.add(point)
			todo.append(point)

	# Return all "seen" skins.
	return seen

def snake_finder(head, skins):
	jump = {
		"<": lambda p: (p[0] + 1, p[1]),
		">": lambda p: (p[0] - 1, p[1]),
		"^": lambda p: (p[0], p[1] + 1),
		"v": lambda p: (p[0], p[1] - 1),
	}.get(head[1])

	# Get the skin "path".
	start = jump(head[0])
	path = bfs(start, skins)

	# Size + head.
	return len(path) + 1

def main():
	head, skins = load_room("room.txt")
	size = snake_finder(head, skins)
	print(size)

if __name__ == "__main__":
	main()
