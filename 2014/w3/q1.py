#!/usr/bin/env python3
# Enter your code for "Rövarspråket!" here.

import re

def encode(string):
	def _repl(match):
		m = match.group(1)

		if string.islower() or string.istitle() or m.islower():
			return "%so%s" % (m, m.lower())
		else:
			return "%sO%s" % (m, m.upper())

	return re.sub(r"([b-df-hj-np-tv-z])", _repl, string, flags=re.I)

def decode(string):
	return re.sub(r"([b-df-hj-np-tv-z])o\1", r"\1", string, flags=re.I)

