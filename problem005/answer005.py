#!/usr/bin/python

def no_remainders(n,max_multiplier):
	check = 1
	while check <= max_multiplier:
		if (n % check) != 0:
			return False
		check += 1

	return True

n = 1
max_multiplier = 20

while True:
	if no_remainders(n,max_multiplier):
		#print n
		break
	n += 1

print "ANSWER:" + str(n)
