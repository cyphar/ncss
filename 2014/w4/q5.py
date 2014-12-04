#!/usr/bin/env python3
# Enter your code for "Bejeweled I" here.

def find_groups(line, num=3, exclude=frozenset({"?"})):
	"Finds all groups of length num and then yields their respective (start, end) indexes."

	for start, _ in enumerate(line):
		group = line[start:start+num]

		# Ensure group length is maintained.
		if len(group) != num:
			continue

		# Check that items aren't in the exclude list.
		if any(item in exclude for item in group):
			continue

		# Check that all items are equal.
		if all(group[0] == item for item in group):
			yield (start, start+num)

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
			for match in find_groups(line, num=3, exclude={"?"}):
				for x in range(match[0], match[1]):
					pos = Position(x, y)
					removes.append(pos)

				delta += 10

		# Find vertical matches.
		for y, line in enumerate(zip(*self.lines)):
			for match in find_groups(line, num=3, exclude={"?"}):
				for x in range(match[0], match[1]):
					pos = Position(y, x)
					removes.append(pos)

				delta += 10

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
