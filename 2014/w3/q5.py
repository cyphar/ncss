#!/usr/bin/env python3
# Enter your code for "Particle Class" here.

import math

class Particle(object):
	def __init__(self, x, y, vx, vy, q):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.q = q

	def disp(self):
		print("position = (%d, %d)" % (self.x, self.y))
		print("velocity = (%d, %d)" % (self.vx, self.vy))
		print("charge = %d" % (self.q,))

	def move(self):
		self.x += self.vx
		self.y += self.vy

	def distance(self, otherx, othery):
		return math.sqrt((self.x - otherx) ** 2 + (self.y - othery) ** 2)
