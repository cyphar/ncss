#!/usr/bin/env python2

def code(col,msg):
    peeps = []
    for x in col:
        worked = True
        if len(x) > len(msg):
            worked = False
        else:
            for y in x: #each char
                if y not in msg[x.index(y)]:
                    worked = False
        if worked:
            peeps.append(x)
    return peeps

for x in code(raw_input("Who are your collegues? ").split(), raw_input("What is the message? ").split()):
    print x,"could have written this."
