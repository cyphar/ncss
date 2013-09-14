#!/usr/bin/env python3
# Enter your code for "Costly cake!" here.

cakes = []

for x in range(2):
	i = x + 1

	tmp = {
		"id"	: i,
		"size"	: float(input("Cake %d side length (cm): " % (i))) ** 2,
		"cost"	: float(input("Cake %d cost ($): " % (i)))
	}

	tmp["per"] = tmp["cost"] / tmp["size"]
	cakes.append(tmp)


for x in sorted(cakes, key=lambda x: x["id"]):
	print("Cake %d costs $%.2f per cm2 for %.0f cm2" % (x["id"], x["per"], x["size"]))

srt = sorted(cakes, key=lambda x: x["per"])

if not all(x["per"] == srt[0]["per"] for x in srt):
	print("Get cake %d!" % (srt[0]["id"]))
else:
  	print("Get either!")
