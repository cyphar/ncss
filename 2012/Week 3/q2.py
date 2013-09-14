#!/usr/bin/env python2

msg = str(raw_input("Message: "))
msg = msg.lower()
w = msg.split(' ')
l = msg.split(' ')
i = 0
final = ''
while i < len(w):
	if w.count(w[i]) != 1:
		w.remove(w[i])
	else:
		i+=1
for x in w:
	l.remove(x)
for each in range(len(l)):
	final += l[each]+" "
if l != list():
	print final
