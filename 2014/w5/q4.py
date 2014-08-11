#!/usr/bin/env python3
# Enter your code for "Particle Simulator" here.

class Particle(object):
	def __init__(self, x, y, vx, vy, q, ax, ay):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.q = q
		self.ax = ax
		self.ay = ay

	def accelerate(self):
		self.vx += self.ax
		self.vy += self.ay

	def move(self):
		self.x += self.vx
		self.y += self.vy


def load_particles(path):
	with open(path) as f:
		lines = [line.strip() for line in f]

	steps = int(lines[0])

	particles = []
	for line in lines[1:]:
		if not line:
			continue

		fields = line.split()
		particle = Particle(*map(float, fields))
		particles.append(particle)

	return steps, particles


class System(object):
	def __init__(self, particles):
		# Particle system.
		self.particles = particles

		# Borders.
		self.left = -300
		self.right = 300
		self.top = 200
		self.bottom = -200

	def _step_acceleration(self, particle):
		# Get all particles to left and right of particle in system.
		left = [other for other in self.particles if other.x < particle.x]
		right = [other for other in self.particles if other.x > particle.x]

		# Get the left and right components of the new horizontal acceleration.
		axleft = len([other for other in left if other.q == -particle.q]) + len([other for other in right if other.q == particle.q])
		axright = len([other for other in right if other.q == -particle.q]) + len([other for other in left if other.q == particle.q])

		# Calculate horizontal acceleration.
		particle.ax = (axright - axleft) / 10.0

		# Get all particles above and below particle in system.
		top = [other for other in self.particles if other.y > particle.y]
		bottom = [other for other in self.particles if other.y < particle.y]

		# Get the top and bottom components of the new vertical acceleration.
		axtop = len([other for other in top if other.q == -particle.q]) + len([other for other in bottom if other.q == particle.q])
		axbottom = len([other for other in bottom if other.q == -particle.q]) + len([other for other in top if other.q == particle.q])

		# Calculate vertical acceleration.
		particle.ay = (axtop - axbottom) / 10.0

	def _step_bounce(self, particle):
		if particle.x <= self.left:
			particle.x = self.left
			particle.vx = -particle.vx

		if particle.x >= self.right:
			particle.x = self.right
			particle.vx = -particle.vx

		if particle.y >= self.top:
			particle.y = self.top
			particle.vy = -particle.vy

		if particle.y <= self.bottom:
			particle.y = self.bottom
			particle.vy = -particle.vy

	def step(self):
		for particle in self.particles:
			self._step_acceleration(particle)

		for particle in self.particles:
			particle.accelerate()
			particle.move()
			self._step_bounce(particle)

	def snap(self):
		return [(particle.x, particle.y) for particle in self.particles]


def fmt(snap):
	flat = [val for pos in snap for val in pos]
	return ",".join("%.1f" % (val,) for val in flat)

def main():
	steps, particles = load_particles("particles.txt")
	system = System(particles)

	simulation = []
	for _ in range(steps):
		system.step()

		snap = system.snap()
		simulation.append(snap)

	for step in simulation:
		print(fmt(step))

if __name__ == "__main__":
	main()
