#!/usr/bin/env python2

msg = str(raw_input("Message: ")).lower().split()
w = set(msg)

for word in w:
	if word in msg:
		msg.remove(word)

if len(msg):
	print " ".join(msg)
