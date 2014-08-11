#!/usr/bin/env python2

t = open("tweet_list.txt", "rU").read().split("\n")
r = []
for x in open("rhymes.txt", "rU").read().split("\n"):
    for y in x.split():
        if ":" in y:
            r.append(y.split(":")[0])
            r.append(y.split(":")[1])
        else:
            r.append(y)

def rhymes(word1,word2):
    mid = r.index(word1)
    for point in range(mid,0,-1):
        if r[point].isdigit():
            start = int(r[point])
            end = int(r[point]) + 1
            break
    #print r.index(str(start)),mid,r.index(str(end))
    if word2 in r[r.index(str(start))+1:r.index(str(end))]:
        return True
    else:
        return False

def find(orig):
    last = orig.split()[-1].lower()
    final = orig +"\n"
    z = int(1)
    for a in range(len(t)-1):
        if z < 5:
            if rhymes(last,t[a].split()[-1].lower()):
                final += t[a] + "\n"
                z += 1
    return final[:-1]

print find(raw_input("First line: "))
