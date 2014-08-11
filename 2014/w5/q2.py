#!/usr/bin/env python3
# Enter your code for "Bracket Mountains" here.

BRACKETS = {
	"{": "}",
	"(": ")",
}

def parse(tokens, end=None, depth=0):
	nodes = []

	# Parse loop.
	while tokens:
		# Pop off front token.
		startb, *tokens = tokens

		# Opening bracket found.
		if startb in BRACKETS:
			# Recursively parse tokens.
			endb = BRACKETS[startb]
			subnodes, tokens = parse(tokens, end=endb, depth=depth+1)

			# Detected an error.
			if subnodes is None:
				return None, tokens

			# Update tokens.
			nodes += [(startb, depth)] + subnodes + [(endb, depth)]

		# Got to the end -- break out.
		elif startb == end:
			break

		# Invalid character.
		else:
			return None, tokens

	return nodes, tokens

def main():
	# Parse input.
	line = input()
	nodes, _ = parse(line)

	# Invalid input.
	if nodes is None:
		print("Invalid input!")
		return

	# Get maximum depth
	max_depth = max(nodes, key=lambda n: n[1])[1]
	for depth in range(max_depth+1)[::-1]:
		out = []

		# Space out nodes of the wrong depth.
		for t, d in nodes:
			if d == depth:
				out.append(t)
			else:
				out.append(" ")

		print("".join(out))

if __name__ == "__main__":
	main()
