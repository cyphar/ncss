#!/usr/bin/env python3
# Enter your code for "Bejeweled I" here.

import re

class Position(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Grid(object):
	def __init__(self, lines):
		self.lines = lines

	def display(self, score=0):
		for row in self.lines:
			print(*row)
		print("Score = %d" % (score,))

	def removal(self):
		delta = 0
		removes = []

		# Find horizontal matches.
		for y, line in enumerate(self.lines):
			for match in re.finditer(r"([^?])\1\1\1*", "".join(line)):
				for x in range(match.start(), match.end()):
					pos = Position(x, y)
					removes.append(pos)

				delta += 10 + 10 * (match.end() - match.start() - 3)

		# Find vertical matches.
		for y, line in enumerate(zip(*self.lines)):
			for match in re.finditer(r"([^?])\1\1\1*", "".join(line)):
				for x in range(match.start(), match.end()):
					pos = Position(y, x)
					removes.append(pos)

				delta += 10 + 10 * (match.end() - match.start() - 3)

		# Remove the scheduled removals.
		for remove in removes:
			self.lines[remove.y][remove.x] = None

		return delta

	def cascade(self):
		# Columns are easier to deal with.
		columns = []
		for column in zip(*self.lines):
			# Strip "" and pad the top.
			stripped = [cell for cell in column if cell is not None]
			padding = ["?"] * (len(column) - len(stripped))

			# Append column.
			columns.append(padding + stripped)

		# Covert back to rows.
		self.lines = [list(row) for row in zip(*columns)]


def load_grid(path):
	with open(path) as f:
		# Get data.
		data = f.read().strip()

		# Break data down into 8-cell chunks.
		grid = [list(line) for line in zip(*[iter(data)]*8)]

	return Grid(grid[::-1])

def main():
	# Start with a score of 0.
	score = 0

	# Load the grid.
	grid = load_grid("jewels.txt")
	grid.display(score)

	# Solve loop.
	while True:
		delta = grid.removal()

		# No removals.
		if not delta:
			break

		score += delta
		grid.cascade()

	# Final output.
	grid.display(score)


if __name__ == "__main__":
	main()
