#!/usr/bin/env python3
# Enter your code for "Expand This!" here.

class Term:
	def __init__(self, mult, exp):
		self.mult = mult # co-efficient
		self.exp = exp # power of pronumeral

	def __add__(self, other):
		if self.exp == other.exp:
			return [Term(self.mult + other.mult, self.exp)]
		else:
			return [self, other]

	def __sub__(self, other):
		if self.exp == other.exp:
			return [Term(self.mult - other.mult, self.exp)]
		else:
			return [self, other]

	def __mul__(self, other):
		return [Term(self.mult * other.mult, self.exp + other.exp)]

	def __pow__(self, other):
		return [Term(self.mult ** other.mult, self.exp * other.mult)]

	def __str__(self):
		exp = ""

		if abs(self.exp) > 1:
			exp = "^%d" % self.exp

		mult = ""
		if self.mult == -1 and self.exp:
			mult = "-"
		elif abs(self.mult) > 1 or not self.exp:
			mult = "%d" % self.mult

		num = ""
		if self.exp:
			num = "x"

		return "%s%s%s" % (mult, num, exp) or "0"

	def __repr__(self):
		return self.__str__()

def isop(tok):
	return tok in ["+", "-", "*", "^"]

def isword(tok):
	return not isop(tok)

tokens = input("RPN: ").split()
stack = []

for i in tokens:
	if isword(i):
		s = []

		# Get correct exponent of x and coefficient of x
		if i == "x":
			s = [Term(1, 1)]
		elif i == "-x":
			s = [Term(-1, 1)]
		else:
			s = [Term(int(i), 0)]

		stack.append(s)

	if isop(i):
		# get arguments
		arg2 = stack.pop()
		arg1 = stack.pop()

		# get operator lambda
		op = {
			"+" : lambda x,y:x+y,
			"-" : lambda x,y:x-y,
			"*" : lambda x,y:x*y,
			"^" : lambda x,y:x**y,
		}.get(i)

		out = []

		if i in "*":
			for a in arg1:
				for b in arg2:
					out += op(a, b)
		elif i in "^":
			# to make expansion simpler, powers are just multiplication of items in brackets
			tmp = [arg1] * arg2[0].mult

			while len(tmp) >= 2:
				# get items
				x, y = tmp.pop(), tmp.pop()
				n = []

				# multiply all of them together
				for a in x:
					for b in y:
						n += a * b

				tmp = [n] + tmp

			if not tmp:
				out = [Term(1, 0)]
			else:
				out = tmp[0][:]
		else:
			# Add together the groups, using the signing chosen by the above operator
			out = [a for a in arg1] + [c for b in arg2 for c in op(Term(0, b.exp), b)]

		stack.append(out)

# Simplify this spruce goose
stack = [y for x in stack for y in x]
stack = sorted(stack, key=lambda n:-n.exp)

tmp = [[stack[0]]]
for x in stack[1:]:
	# Group same exponents of x
	if x.exp == tmp[-1][0].exp:
		tmp[-1].append(x)
	else:
		tmp.append([x])

simple = []
for group in tmp:
	n = [Term(0, group[0].exp)]

	# Add all terms together
	for term in group:
		n = n[0] + term

	simple.append(n)

# Flatten list
stack = [y for x in simple for y in x]

out = ""
if stack:
	out = "%s" % stack[0]
	for x in stack[1:]:
		if x.mult:
			# Split out sign from term and then just add a term with the same magnitude of mult
			out += " %c %s" % ("+-"[x.mult < 0], Term(abs(x.mult), x.exp))

print(out or "0")
