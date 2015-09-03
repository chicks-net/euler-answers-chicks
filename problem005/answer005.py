#!/usr/bin/python
"""chicks' answer to Euler Project problem #5"""

def no_remainders(n, max_multiplier):
	check = 1
	while check <= max_multiplier:
		if (n % check) != 0:
			return False
		check += 1

	return True

n = 2
max_multiplier = 20

while True:
	if no_remainders(n, max_multiplier):
		#print n
		break
	n += 2

print "ANSWER:" + str(n)
