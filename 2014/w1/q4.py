#!/usr/bin/env python3
# Enter your code for "Soccer Draw" here.

def group(lst, n):
	for i in range(0, len(lst), n):
		val = lst[i:i+n]
		if len(val) == n:
			yield tuple(val)

def get_round(teams, iteams):
	rnd = 1
	while len(teams) > 1:
		nteams = []
		for match in group(teams, 2):
			if {c[0] for c in match} == iteams:
				return rnd

			winner = min(match, key=lambda c: c[1])
			nteams.append(winner)

		teams = nteams
		rnd += 1

def main():
	iteams = {input(), input()}

	teams = []
	with open("draw.txt") as f:
		for line in f:
			fields = line.strip().split(",")

			country = (fields[0], int(fields[1]))
			teams.append(country)

	rnd = get_round(teams, iteams)
	if rnd is None:
		print("Did not play")
	else:
		print("Round %d" % rnd)

if __name__ == "__main__":
	main()
