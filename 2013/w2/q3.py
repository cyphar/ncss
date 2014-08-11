#!/usr/bin/env python3
# Enter your code for "No Vowel Sort" here.

def novowelsort(unsorted):
	return sorted(unsorted, key=lambda item:"".join(char for char in item if char.lower() not in "aeiou"))
