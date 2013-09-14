#!/usr/bin/env python3
# Enter your code for "Graph lOOkup" here.

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

class ParseException(Exception):
	pass

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

	def graph_search(self, node, query):
		"""
		Runs a facebook-graphs-like search on
		the current graph, using SQL-like syntax

		The node is the node in the network requesting
		the query
		"""

		"""
		<query> ::= <n_query> | <g_query>
		<n_query> ::= "NEIGHBOURS WHO HAVE" <n_conditions> | "ALL NEIGHBOURS"
		<n_conditions> ::= <n_and_condition> | <n_and_condition> "OR" <n_and_condition>
		<n_and_condition> ::= <n_condition> | <n_condition> "AND" <n_condition>
		<n_condition> ::= <label_condition> | <node_label_condition> | <neighbour_num_condition> | "(" <n_conditions> ")"

		<label_condition> ::= "LABEL" <label>
		<node_label_condition> ::= "NEIGHBOUR LABEL" <label>
		<neighbour_num_condition> ::= <num_condition> | <num_label_condition>
		<num_operator> ::= "EXACTLY" | "LESS THAN" | "MORE THAN"
		<num_condition> ::= <num_operator> <num> "NEIGHBOURS"
		<num_label_condition> ::= <num_operator> <num> "NEIGHBOURS WITH LABEL" <label>

		<g_query> ::= "PEOPLE WHO HAVE" <g_conditions>
		<g_conditions> ::= <g_and_condition> | <g_and_condition> "OR" <g_and_condition>
		<g_and_condition> ::= <g_condition> | <g_condition> "AND" <g_condition>
		<g_condition> ::= <neighbour_num_condition> | <degrees_condition> | "(" <g_conditions> ")"
		<degrees_condition> ::= <num> "DEGREES OF SEPARATION FROM ME"
		"""

		def pop(tokens, legal, off=0):
			if tokens:
				for t in legal:
					n = len(t.split())

					token = ' '.join(tokens[off:n+off])

					if token.lower() == t.lower():
						for x in range(n):
							if len(tokens) > off:
								tokens.pop(off)
						return t

		# overall query
		def q(tokens):
			a = g_query(tokens)

			if a == None:
				a = n_query(tokens)

			if a == None or tokens:
				raise ParseException

			return sorted(a, key=lambda n:n.id)

		# N queries
		def n_query(tokens):
			cond = None

			if pop(tokens, ["NEIGHBOURS WHO HAVE"]) and tokens:
				cond = n_conds(tokens)
				if not cond:
					raise ParseException

			elif pop(tokens, ["ALL NEIGHBOURS"]):
				cond = lambda n1,n2:True
				if tokens:
					raise ParseException

			if cond:
				return [N for n in node.neighbours.values() for N in n if cond(node, N)]

		def n_conds(tokens):
			cond = n_and_cond(tokens)

			if cond and pop(tokens, ["OR"]):
				a = n_and_cond(tokens)
				if a:
					cond = lambda n1,n2,a=a,cond=cond:(a(n1, n2) or cond(n1, n2))
				else:
					raise ParseException

			return cond

		def n_and_cond(tokens):
			cond = n_cond(tokens)

			if cond and pop(tokens, ["AND"]):
				a = n_cond(tokens)
				if a:
					cond = lambda n1,n2,a=a,cond=cond:(a(n1, n2) and cond(n1, n2))
				else:
					raise ParseException

			return cond

		def n_cond(tokens):
			cond = label_cond(tokens) or node_label_cond(tokens) or neighbour_num_cond(tokens)

			if not cond and pop(tokens, ["("]):
				tmp = n_conds(tokens)
				if tmp and pop(tokens, [")"]):
					cond = tmp
				else:
					raise ParseException

			return cond

		def num_operator(tokens):
			return pop(tokens, ["EXACTLY"]) or pop(tokens, ["LESS THAN"]) or pop(tokens, ["MORE THAN"])

		def num_label_cond(tokens):
			op = {
				"EXACTLY" : lambda a,b:a==b,
				"LESS THAN" : lambda a,b:a<b,
				"MORE THAN" : lambda a,b:a>b
			}.get(num_operator(tokens), None)
			num = None

			if op and tokens:
				g = tokens.pop(0)
				if g.isnumeric():
					num = int(g)
					if pop(tokens, ["NEIGHBOURS WITH LABEL"]) and tokens:
						l = tokens.pop(0)
						return lambda n1,n2,num=num,l=l:op(len(n2.neighbours.get(l, [])), num)
					elif pop(tokens, ["NEIGHBOURS"]):
						return lambda n1,n2,num=num:op(len([y for x in n2.neighbours.values() for y in x]), num)

		def neighbour_num_cond(tokens):
			return num_label_cond(tokens)

		# General conditions
		def label_cond(tokens):
			if pop(tokens, ["LABEL"]) and tokens:
				l = tokens.pop(0)
				return lambda n1,n2,l=l:(n2.label == l)

		def node_label_cond(tokens):
			if pop(tokens, ["NEIGHBOUR LABEL"]) and tokens:
				l = tokens.pop(0)
				return lambda n1,n2,l=l:(n2 in n1.neighbours.get(l, []))

		# G queries
		def g_query(tokens):
			cond = None

			if pop(tokens, ["PEOPLE WHO HAVE"]) and tokens:
				cond = g_conds(tokens)
				if not cond:
					raise ParseException

			if cond:
				return [N for N in self.nodes.values() if cond(node, N)]

		def g_conds(tokens):
			cond = g_and_cond(tokens)

			if cond and pop(tokens, ["OR"]):
				a = g_and_cond(tokens)
				if a:
					cond = lambda n1,n2,a=a,cond=cond:(a(n1, n2) or cond(n1, n2))
				else:
					raise ParseException

			return cond

		def g_and_cond(tokens):
			cond = g_cond(tokens)

			if cond and pop(tokens, ["AND"]):
				a = g_cond(tokens)
				if a:
					cond = lambda n1,n2,a=a,cond=cond:(a(n1, n2) and cond(n1, n2))
				else:
					raise ParseException

			return cond

		def g_cond(tokens):
			cond = neighbour_num_cond(tokens) or deg_cond(tokens)

			if not cond and pop(tokens, ["("]) and tokens:
				tmp = g_conds(tokens)
				if tmp and pop(tokens, [")"]):
					cond = tmp
				else:
					raise ParseException

			return cond

		def deg_cond(tokens):
			if pop(tokens, ["DEGREES OF SEPARATION FROM ME"], 1) and tokens:
				t = int(tokens.pop(0))
				return lambda n1,n2:(self.degrees_of_separation(n2.id, n1.id) == t)

		return q(query.split())

if __name__ == "__main__":
	graph = Graph('graph', None)
	graph.load('test.txt')

	graph.output()

	import readline

	sel = graph.get_node('0')
	for x in iter(lambda:input(">>> "), ""):
		if ':' in x:
			sel = graph.get_node(x.split(':')[0])
			q = x.split(':')[1]
		else:
			q = x

		try:
			for x in graph.graph_search(sel, q):
				print("%s" % x)
		except (ParseException, ValueError) as e:
			print(type(e))
