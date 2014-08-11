#!/usr/bin/env python3
# Enter your code for "Aardvark!" here.

import re

def main():
	line = input()

	pattern = ".*".join("aardvark")
	if re.search(pattern, line, re.I):
		print("Aardvark!")
	else:
		print("No aardvarks here :(")

if __name__ == "__main__":
	main()
