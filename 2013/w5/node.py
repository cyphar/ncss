class Node:
  def __init__(self, id, label):
    self.id = id
    self.label = label
    self.neighbours = {}

  def __str__(self):
    return "({0}: {1})".format(self.id, self.label)

  def add_neighbour(self, neighbour, label):
    if label in self.neighbours:
      self.neighbours[label].append(neighbour)
    else:
      self.neighbours[label] = [neighbour]

  def _build_neighbours(self):
    neighbours = []
    for key in self.neighbours:
      neighbours.extend(self.neighbours[key])
    return neighbours

  def get_neighbours(self, label):
    if label is None:
      return self._build_neighbours()
    else:
      return self.neighbours.get(label, [])

  def degree(self, label):
    if label is None:
      return len(self._build_neighbours())
    else:
      return len(self.neighbours.get(label, []))

  def has_neighbour(self, node, label):
    neighbours = self.neighbours.get(label, [])
    if label is None:
      neighbours = self._build_neighbours()

    for n in neighbours:
      if n.id == node.id and n.label == node.label:
        return True
    return False
