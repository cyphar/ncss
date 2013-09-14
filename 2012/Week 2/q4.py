#!/usr/bin/env python2

import sys
wide = int(raw_input("How wide is the pit? "))
deep = int(raw_input("How deep is the pit? "))
ball = 1
move = "right"
line = ""
this = 0

for level in range(0,deep):
    line = "#" #begin

    for point in range(1,wide + 1):
        if this == 0:
            if point == ball:
                line += "*" #ball is here
                this = 1
                if move == "left":
                    ball -= 1
                if move == "right":
                    ball += 1
                if ball == wide:
                    move = "left"
                if ball == 1:
                    move = "right"
            else:
                line += " " #nothing here
        else:
            line += " " #ball already exists

    line += "#\n" #end
    this = 0
    sys.stdout.write(line)
