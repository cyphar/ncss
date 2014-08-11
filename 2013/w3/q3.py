#!/usr/bin/env python3
# Enter your code for "Graph nOOde" here.

class Node:
	def __init__(self, id, label):
		"""
		Initialise a node with a given id and label
		"""

		self.id = id
		self.label = label
		self.neighbours = {}

	def __str__(self):
		"""
		Return a string representation of the node
		as "(id: label), e.g. (4: Greg)"
		"""
		return "(%d: %s)" % (self.id, self.label)

	def __repr__(self):
		"""
		Return a string representation of the node
		as "(id: label), e.g. (4: Greg)"
		"""
		return self.__str__()

	def add_neighbour(self, neighbour, label):
		"""
		Add a neighbour to this node with
		a given edge label
		e.g. x.add_neighbour(y, "brother")
		"""

		if label not in self.neighbours:
			self.neighbours[label] = []

		self.neighbours[label].append(neighbour)

	def _all_neighbours(self):
		neighbours = []

		for label in self.neighbours.values():
			for node in label:
				neighbours.append(node)

		return neighbours

	def get_neighbours(self, label):
		"""
		Returns a list of node objects that are
		neighbours of this node with a given edge label
		Return an empty list if there are no neighbours
		with the given label
		Return all neighbours if label is None
		e.g. x.get_neighbours("brother")
		"""
		if label is None:
			return self._all_neighbours()

		elif label in self.neighbours:
			return self.neighbours[label]

		else:
			return []

	def degree(self, label):
		"""
		Returns the number of neighbours with a given
		edge label
		Return total number of neighbours
		if label is None
		"""
		if label is None:
			return len(self._all_neighbours())

		elif label in self.neighbours:
			return len(self.neighbours[label])

		else:
			return 0

	def has_neighbour(self, node, label):
		"""
		Returns True if this node has 'node' as a
		neighbour with a given label, False otherwise
		Returns True if this node has 'node' as a
		neighbour if label is None, False otherwise
		"""
		if label is None:
			return node in self._all_neighbours()

		elif label in self.neighbours:
			return node in self.neighbours[label]

		return False


if __name__ == "__main__":
	n1 = Node(1, "a1")
	n1.add_neighbour(Node(2, "b2"), "b")
	n1.add_neighbour(Node(3, "b3"), "b")
	n1.add_neighbour(Node(4, "c4"), "c")
	print(n1.degree(None))  # Should be 3
	print(n1.degree("b"))  # Should be 2
	print(n1.degree("c"))  # Should be 1
	print(n1.degree("d"))  # Should be 0

	print(n1.get_neighbours(None))  # Should return a list of the 3 neighbour nodes
	print(n1.get_neighbours("b"))  # Should return a list of the first two nodes
	print(n1.get_neighbours("c"))  # Should return a list of the last node
	print(n1.get_neighbours("d"))  # Should return []

	n5 = Node(5, "d5")
	n1.add_neighbour(n5, "c")
	print(n1.has_neighbour(n5, None))  # Should be True
	print(n1.has_neighbour(n5, "c"))  # Should be True
	print(n1.has_neighbour(n5, "b"))  # Should be False
	print(n1.has_neighbour(None, "c"))  # Should be False
