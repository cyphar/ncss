#!/usr/bin/env python3
# Enter your code for "Rolling Balls" here.

class Hole(object):
	def __init__(self, diameter, capacity):
		self.diameter = diameter
		self.capacity = capacity
		self.contents = []

	def can_fit(self, ball):
		return len(self.contents) < self.capacity and ball.diameter <= self.diameter

	def add_ball(self, ball):
		self.contents.append(ball)

class Ball(object):
	def __init__(self, diameter, label):
		self.diameter = diameter
		self.label = label

	def roll(self, holes):
		for hole in holes:
			if hole.can_fit(self):
				return hole

def main():
	holes = []
	with open("holes.txt") as f:
		for line in f:
			line = line.strip()

			if not line:
				continue

			diameter, capacity = line.split()

			hole = Hole(int(diameter), int(capacity))
			holes.append(hole)

	balls = []
	with open("balls.txt") as f:
		for line in f:
			line = line.strip()

			if not line:
				continue

			diameter, label = line.split()

			ball = Ball(int(diameter), label)
			balls.append(ball)

	bucket = []
	for ball in balls:
		hole = ball.roll(holes)

		if hole:
			hole.add_ball(ball)
		else:
			bucket.append(ball)

	if bucket:
		items = ", ".join(ball.label for ball in bucket)
		print("The bucket contains: %s." % (items,))
	else:
		print("The bucket contains no balls.")

if __name__ == "__main__":
	main()
