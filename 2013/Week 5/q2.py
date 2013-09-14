#!/usr/bin/env python3
# Enter your code for "Interleaving" here.

def interleavings(s1, s2):
	def interleave(s1, s2):
		if not s1 or not s2:
			# return the rest of either string or ""
			return [s1 or s2]
		else:
			# basically make and return a binary tree recursively
			return [s1[0] + n for n in interleave(s1[1:], s2)] + [s2[0] + n for n in interleave(s1, s2[1:])]

	# sort and make the items unique
	return sorted(n for n in set(interleave(s1, s2)))

if __name__ == "__main__":
	print(interleavings(input(), input()))
