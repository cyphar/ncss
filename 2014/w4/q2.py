#!/usr/bin/env python3
# Enter your code for "Particle Reader" here.

import particle

def load_particles(filename):
	particles = []
	with open(filename) as f:
		for num, line in enumerate(f):
			line = line.strip()

			# Skip dummy lines.
			if not line:
				continue

			fields = line.split()

			# Invalid number of fields.
			if len(fields) > 5:
				raise RuntimeError("Line %d contains too many items" % (num+1,))
			elif len(fields) < 5:
				raise RuntimeError("Line %d contains too few items" % (num+1,))

			# Try to convert to number.
			try:
				x, y, vx, vy, q = map(float, fields)
			except ValueError:
				raise TypeError("Line %d has a non-number" % (num+1,))

			# Check for invalid charge.
			if q not in [-1, 0, 1]:
				raise ValueError("Line %d has an invalid charge" % (num+1,))

			# Check if particle in previous particle positions.
			if (x, y) in ((p.x, p.y) for p in particles):
				raise ValueError("Line %d uses the same position as a previous particle" % (num+1,))

			# Create particle.
			part = particle.Particle(x, y, vx, vy, q)
			particles.append(part)

	return particles

def main():
	print(load_particles("particles.txt"))

if __name__ == "__main__":
	main()
