#!/usr/bin/env python3
# Enter your code for "Bejeweled II" here.

# I ... don't want to talk about it.
import copy

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

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return "(%r, %r)" % (self.x, self.y)


class Grid(object):
	def __init__(self, lines, fills):
		self._lines = lines
		self._fills = iter(fills or [])

	def display(self, score=0):
		for row in self._lines[::-1]:
			print(*row)

		print("Score = %d" % (score,))

	def removal(self):
		delta = 0
		removes = []

		# Find horizontal matches.
		for y, line in enumerate(self._lines):
			for match in find_groups(line, num=3):
				for x in range(match[0], match[1]):
					pos = Position(x, y)
					removes.append(pos)

				delta += 10

		# Find vertical matches.
		for x, column in enumerate(zip(*self._lines)):
			for match in find_groups(column, num=3):
				for y in range(match[0], match[1]):
					pos = Position(x, y)
					removes.append(pos)

				delta += 10

		# Remove the scheduled removals.
		for remove in removes:
			self._lines[remove.y][remove.x] = None

		return delta

	def cascade(self):
		# Columns are easier to deal with.
		columns = []
		for column in zip(*self._lines[::-1]):
			# Strip "" and pad the top.
			stripped = [cell for cell in column if cell is not None]
			padding = [None] * (len(column) - len(stripped))

			# Append column.
			columns.append(padding + stripped)

		# Covert back to rows.
		self._lines = [list(row) for row in zip(*columns)][::-1]

	def fill(self):
		# Convert to columns to get priority right.
		columns = zip(*self._lines)

		# Fill from left->right, bottom->top.
		for x, column in enumerate(columns):
			for y, cell in enumerate(column):
				# Check if cell needs to be replaced.
				if cell is None:
					self._lines[y][x] = next(self._fills)

	def swap(self, left, right):
		# Out of bounds.
		if min(left.x, left.y, right.x, right.y) < 0:
			return False

		# Out of bounds.
		if max(left.x, left.y, right.x, right.y) > 7:
			return False

		dx = abs(left.x - right.x)
		dy = abs(left.y - right.y)

		# Invalid deltas.
		if (dx, dy) not in [(1, 0), (0, 1)]:
			return False

		# Swap away (do it in a copy, so reverting is simple).
		new = copy.deepcopy(self._lines)
		new[left.y][left.x], new[right.y][right.x] = new[right.y][right.x], new[left.y][left.x]

		# Create a fake grid.
		fakegrid = copy.deepcopy(new)
		fake = Grid(fakegrid, None)

		# Check if move will result in a removal.
		if not fake.removal():
			return False

		# Move is valid, update actual grid.
		self._lines = new
		return True

	def solve(self):
		score = 0
		multiplier = 0

		# Solve loop.
		while True:
			delta = self.removal()

			# No removals.
			if not delta:
				break

			# Update multiplier and add to score.
			multiplier += 1
			score += delta * multiplier

			# Cascade and fill the gaps.
			self.cascade()
			self.fill()

		return score


def load_grid(path):
	with open(path) as f:
		# Get data.
		data = f.read().strip()

		# Split data into grid data and fill data.
		data, fill = data[:64], data[64:]

		# Break data down into 8-cell chunks.
		grid = [list(line) for line in zip(*[iter(data)]*8)]

	return Grid(grid, fill)

def main():
	# Start with a score of 0.
	score = 0

	# Load the grid.
	grid = load_grid("jewels.txt")
	grid.display(score)

	for line in iter(input, ""):
		# Get move.
		fields = line.split()
		leftx, lefty, rightx, righty = map(int, fields)

		# Check for valid move.
		if not grid.swap(Position(leftx, lefty), Position(rightx, righty)):
			print("Invalid move")
			continue

		# Solve grid move.
		score += grid.solve()

		# Print current state.
		grid.display(score)

if __name__ == "__main__":
	main()
