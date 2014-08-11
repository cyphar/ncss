#!/usr/bin/env python3
# Enter your code for "Optimus SUBlime" here.

def main():
	ingredients = {}

	with open("preferences.txt") as f:
		for line in f:
			line = line.strip()

			ingredient, score = line.split(",")
			ingredients[ingredient] = int(score)

	sandwiches = []

	with open("sandwiches.txt") as f:
		for line in f:
			line = line.strip()

			contains = line.split(",")
			score = sum(ingredients.get(ingredient, 0) for ingredient in contains)

			sandwiches.append((contains, score))

	sandwiches = sorted(sandwiches, key=lambda s: (-s[1], -len(s[0]), ",".join(s[0])))

	for sandwich, score in sandwiches:
		sandwich = ",".join(sandwich)
		print(sandwich)

	if not sandwiches:
		print("devo :(")

if __name__ == "__main__":
	main()
