#!/usr/bin/env python3
# Enter your code for "Graph lOOad" here.

from node import Node
import copy

def bfs(start, end):
	todo = [[start]]
	current = todo[0]

	while len(todo):
		current = todo.pop(0)

		if current[-1] == end:
			return current

		for neighbour in current[-1].get_neighbours(None):
			if neighbour in current or current[-1] == end or not current[-1].has_neighbour(neighbour, None):
				continue

			new = copy.copy(current)
			new.append(neighbour)
			todo.append(new)
	return None

class Graph:
	def __init__(self, label, filename):
		"""
		Initialise a graph with a given label.
		If filename is not None, load the graph from the file
		"""
		self.label = label
		self.nodes = {}

		# Load using .load()
		if filename is not None:
			self.load(filename)

	def size(self):
		"""
		Return the number of nodes in the graph
		"""
		return len(self.nodes)

	def load(self, filename):
		"""
		Load the graph from the given filename.
		Raise ValueError if a node with a duplicate
		id is added or if a relationship between
		nonexisting nodes is created
		"""
		f = open(filename).read().split("\n")

		for item in f:
			command = item.split(":")

			# Add node
			if len(command) == 2:
				_id = command[0].strip()
				_label = command[1].strip() or None

				# Duplicate id
				if _id in self.nodes:
					raise ValueError

				# Add node
				self.nodes[_id] = Node(_id, _label)

			# Add link
			elif len(command) == 3:
				_from = command[0].strip()
				_label = command[1].strip() or None
				_to = command[2].strip()

				# Non-existent Nodes
				if _from not in self.nodes or _to not in self.nodes:
					raise ValueError

				self.nodes[_from].add_neighbour(self.nodes[_to], _label)

	def output(self):
		"""
		Prints the graph with nodes listed in sorted order
		of ids with their neighbours and neighbour labels
		If neighbour labels are None, print the empty
		string.
		Print empty brackets if a node has no neighbours
		e.g.
		(0: Bob) [1:son, 2:wife]
		(1: John) [0:father, 2:mother]
		(2: Jane) [0:husband, 1:son]
		(3: Greg) [1:friend]
		"""
		# Sort graph nodes by id
		nodes = list(self.nodes.values())
		nodes.sort(key=lambda n:n.id)

		for n in nodes:
			# Get all edges
			edges = []
			for edge in n.neighbours:
				for neighbour in n.get_neighbours(edge):
					edges.append((neighbour.id, edge))
			edges.sort()

			# Format edges
			formatted = []
			for edge in edges:
				formatted.append("%s:%s" % (edge[0], edge[1] or ""))

			# Print format
			print("%s [%s]" % (n, ", ".join(formatted)))

	def degrees_of_separation(self, n1, n2):
		"""
		Returns the minimum degrees of separation from
		n1 to n2, where n1 and n2 are ids.
		Each x on the path between n1
		and n2 fulfills the has_neighbour relationship.
		Return -1 if n1 and n2 are not connected.
		Raise ValueError if either n1 or n2 is not in
		this graph
		If n2 is a neighbour of n1, then there is
		1 degree of separation.
		e.g. graph.degrees_of_separation(x, y)
		"""
		# Nodes aren't in graph
		if n1 not in self.nodes or n2 not in self.nodes:
			raise ValueError

		# Get node
		a = self.nodes[n1]
		b = self.nodes[n2]

		# Get shortest distance using BFS
		path = bfs(a, b)

		# Return path length or -1
		if path is not None:
			return len(path) - 1
		else:
			return -1

	def get_node(self, id):
		"""
		Returns the node with the given id
		Raise ValueError if no node with the id exists
		"""
		# No node with given id
		if id not in self.nodes:
			raise ValueError

		return self.nodes[id]

if __name__ == "__main__":
	graph = Graph('graph', None)
	try:
		graph.load("test.txt")
	except ValueError:
		pass

	try:
		graph.load("test2.txt")
	except ValueError:
		pass

	graph.output()
