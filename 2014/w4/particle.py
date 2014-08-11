class Particle:
  def __init__(self, x, y, vx, vy, q):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.q = q

  def disp(self):
    print("position = ({}, {})".format(self.x, self.y))
    print("velocity = ({}, {})".format(self.vx, self.vy))
    print("charge = {}".format(self.q))

  def move(self):
    self.x += self.vx
    self.y += self.vy

  def distance(self, x, y):
    xoff = self.x - x
    yoff = self.y - y
    return (xoff*xoff + yoff*yoff) ** 0.5
