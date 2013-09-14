#!/usr/bin/env python3
# Enter your code for "camelCase" here.

def to_camel(ident):
	ret = ident.split("_")

	camel = ret[0]
	for w in ret[1:]:
		if w:
			camel += w[0].upper() + w[1:]

	return camel
