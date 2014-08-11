#!/usr/bin/env python3
# Enter your code for "Markdown Messaging" here.

import re
import urllib.parse

DEF_PATTERN = r"^\s*\[(.*?)\]:\s*(.*)\s*$"
LINK_PATTERN = r"\[.*?\](\[.*?\]|\(.*?\))"

def get_fragment(link):
	return urllib.parse.urlparse(link).fragment

def main():
	with open("post.md") as f:
		data = f.read()

	refs = {}
	for line in data.split('\n'):
		for ident, link in re.findall(DEF_PATTERN, line):
			refs[ident] = link

	links = []
	for ref in re.findall(LINK_PATTERN, data):
		val = ref[1:-1]

		if re.match(r"\[.*\]", ref):
			link = refs.get(val, "").strip()
		elif re.match(r"\(.*\)", ref):
			link = val.strip()

		links.append(link)

	frags = []
	for link in links:
		frag = get_fragment(link)

		if frag:
			frags.append(frag)

	if frags:
		print(*frags)

if __name__ == "__main__":
	main()
