#!/usr/bin/env python3
# Enter your code for "Image Extractor" here.

import re

site = open("site.html").read()
pattern = r"<\s*img\s+(?:(?:[^>]|['\"].*?['\"])*?\s*src\s*=\s*(['\"])(.+?)\1)+?.*?>"

for match in re.finditer(pattern, site, re.I | re.S):
	print(match.group(2))
