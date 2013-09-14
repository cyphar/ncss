#!/usr/bin/env python3
# Enter your code for "Soccer Scoring" here.

import re

score = open("commentary.txt", "r").read().split("\n")

teams = {}
m = re.match(r"(\w+) versus (\w+)", score[0])

teams[m.group(1)] = 0
teams[m.group(2)] = 0

score = score[1:]

for line in score:
	win = line.split(" ")[0]
	if win:
		teams[win] += 1

score = []

for x in teams:
	score.append((teams[x], x))

score = sorted(score, key=lambda x: x[0], reverse=True)

for team in score:
	print("%s %d" % (team[1], team[0]))
