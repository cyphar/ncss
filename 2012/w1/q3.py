#!/usr/bin/env python2

start = raw_input("Person: ")
if(start == "Knock, knock!"):
	print "Computer: Who's there?"
	who = raw_input("Person: ")
	print "Computer: " + who + " who?"
	lolz = raw_input("Person: ")
	print "Computer: Lol! You got me."
else:
	print "Computer: Sorry, I only talk to people who tell 'knock knock' jokes."
