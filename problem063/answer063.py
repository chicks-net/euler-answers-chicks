#!/usr/bin/python
"""chicks' answer to Euler Project problem #63"""

import sys
import string
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)


def check_powers(k):
	power = len(str(k))
	total_powers = 0
	min = (k-1) ** (1/power)
	for i in xrange(min,min+10):
		check_k = i ** power

		if check_k > k:
#			print "check_k too big k=" + str(k)
			continue

		if k == check_k:
			total_powers = total_powers + 1
			print str(i) + "^" + str(power) + " = " + str(k)
	
	return total_powers

cum_powers = 0
for n in xrange(1,10000000000):
	cum_powers = cum_powers + check_powers(n)

answer = str(cum_powers)
print "ANSWER:" + answer
