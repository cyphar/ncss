#!/usr/bin python3
# Enter your code for "Autobiographical Numbers" here.

inp = input("Number: ")

def is_auto(num):
	if len(num) > 10:
		return False

	for x in range(0, len(num) - 1):
		if int(num[x]) != num.count(str(x)):
			return False

	return True


print("%s is %s" % (inp, "autobiographical" if is_auto(inp) else "not autobiographical"))
