#!/usr/bin/env python2

import math
def snake(rows):
	r = []
	for x in ''.join(rows):
		r.append(x)
	if "@" not in r or "p" not in r:
		return "error";
	leng = len(rows[0])
	final = ""
	a_h = math.ceil(r.index("@") / leng)
	p_h = math.ceil(r.index("p") / leng)
	a_l = r.index("@") % leng
	p_l = r.index("p") % leng
	if a_h > p_h:
		final += "down\n"
	elif a_h < p_h:
		final += "up\n"
	if a_l > p_l:
		final += "right\n"
	elif a_l < p_l:
		final += "left\n"
	return final[:-1]

l = []
while True:
	s = raw_input("Row:")
	if not s:
		break
	l.append(s)
print snake(l)
