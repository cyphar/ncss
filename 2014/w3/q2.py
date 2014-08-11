#!/usr/bin/env python3
# Enter your code for "The Popular Tag" here.

import re
PATTERN = r'<([a-z0-9]+)(?:\s+.*?)?(?:\s*/\s*)?>'

def main():
	with open("input.html") as f:
		data = f.read().lower()

	tags = [tag.lower() for tag in re.findall(PATTERN, data, flags=re.I|re.S)]
	occurs = {tag: tags.count(tag) for tag in set(tags)}

	commons = [(tag, freq) for tag, freq in occurs.items() if freq == max(occurs.values())]
	longests = [(tag, freq) for tag, freq in commons if len(tag) == max(len(t) for t, _ in commons)]

	for tag, freq in longests:
		print("%s %d" % (tag, freq))

if __name__ == "__main__":
	main()
