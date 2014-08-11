#!/usr/bin/env python3
# Enter your code for "Falling Balls" here.

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%r, %r)" % (self.x, self.y)

	def __repr__(self):
		return self.__str__()


class Line(object):
	def __init__(self, p1, p2):
		# Only deal with one case.
		if p1 is None:
			p1, p2 = p2, p1

		# Get leftmost and rightmost points.
		self.left = min((point for point in [p1, p2] if point), key=lambda p: p.x)
		self.right = max((point for point in [p1, p2] if point), key=lambda p: p.x)

		# Gradients.
		self.m = None
		if p2 is not None and p1.x != p2.x:
			self.m = (p1.y - p2.y) / (p1.x - p2.x)

		# Y-intercept.
		self.b = None
		if self.m is not None:
			self.b = p1.y - (self.m * p1.x)

		# There's only an x value.
		self.x = None
		if self.m is None:
			self.x = p1.x

		# Get top and bottom points.
		self.top = self.bottom = None
		if self.m is not None:
			self.top = max((point for point in [p1, p2] if point), key=lambda p: p.y)
			self.bottom = min((point for point in [p1, p2] if point), key=lambda p: p.y)

	def __str__(self):
		if self.x is not None:
			return "[x=%s]" % (self.x,)
		return "[%s, %s]" % (self.top, self.bottom)

	def __repr__(self):
		return self.__str__()

	def intersects(self, other):
		# Only deal with one possibility.
		if self.m is None:
			self, other = other, self

		# Deal with verticals.
		if other.m is None:
			# Does not intersect.
			if other.x < self.left.x or other.x > self.right.x:
				return None

			# Intersects at x.
			x = other.x
			y = (self.m * x) + self.b
			return Point(x, y)

		# Cannot collide.
		if self.m == other.m:
			return None

		# m1x + b1 = m2x + b2
		# (m1 - m2)x + (b1 - b2) = 0
		# x = (b2 - b1)/(m1 - m2)
		x = (other.b - self.b) / (self.m - other.m)
		y = (self.m * x) + self.b

		if self.left <= x <= self.right:
			return Point(x, y)


class Piece(object):
	def __init__(self, label, line):
		self.label = label
		self.line = line

	def __str__(self):
		return "%s:%s" % (self.label, self.line)

	def __repr__(self):
		return self.__str__()


def load_graph(path):
	with open(path) as f:
		marble, *run = f.read().split("\n")

	# Create marble.
	coords = map(float, marble.split())
	marble = Point(*coords)

	pieces = []
	for piece in run:
		if not piece:
			continue

		# Get field values.
		label, *coords = piece.split()
		x1, y1, x2, y2 = map(float, coords)

		# Create line and piece.
		line = Line(Point(x1, y1), Point(x2, y2))
		pieces.append(Piece(label, line))

	return marble, pieces

def main():
	marble, pieces = load_graph("marble-run.txt")

	# Find path through maze.
	path = []
	while marble.y > 0:
		drop = Line(marble, None)
		intersects = [piece for piece in pieces if piece.line.intersects(drop) is not None and piece.line.intersects(drop).y < marble.y]

		# No intersections -- therefore hit the ground.
		if not intersects:
			break

		# Find highest colliding piece.
		piece = max(intersects, key=lambda p: p.line.intersects(drop).y)
		path.append(piece.label)

		# Marble moves to the lowest point.
		marble = piece.line.bottom

		# Remove piece (this deals with IEEE 754 -- why? because I said so).
		pieces.remove(piece)

	path.append("GROUND")
	print(*path)

if __name__ == "__main__":
	main()
