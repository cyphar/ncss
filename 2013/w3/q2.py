#!/usr/bin/env python3
# Enter your code for "Name Cleaning" here.

import re

board = []

for item in open("leaderboard.txt"):
	if not item.strip():
		continue

	score = item.split(',')
	name = score[0].strip()
	points = score[1].strip()

	name = re.sub(r"^[0-9]+", "", name) # REplace leading numbers with ''
	name = re.sub(r"^[A-Z]+(?=[^a-z])", r"", name) # REplace all leading uppercase letters (which aren't followed by a lowercase) with ''
	name = re.sub(r"\b[A-Z]+\b", " ", name) # REplace all UPPERCASE WORDS with ''
	name = re.sub(r"\b[^A-Z].*?\b", " ", name) # REplace all lowercase words with ''

	name = re.sub("\s+", " ", name) # REplace any length of spaces with a single space
	name = name.strip()

	points = int(points.strip())

	# Name has no letters
	if not re.findall("[A-Za-z]", name):
		name = "Invalid Name"

	board.append([name, points])

# First sort by name, then by score
board.sort(key=lambda x:(-x[1], x[0]))

for student in board:
	print("%s,%d" % (student[0], student[1]))
