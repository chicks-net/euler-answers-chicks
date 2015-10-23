#!/usr/bin/python
"""chicks' answer to Euler Project problem #16"""

import math

max_factor = 100

def calc_digit_sum(n):
	digits = list(str(n))
	sum = 0
	for digit in digits:
		sum += int(digit)

	#print str(n) + " -> " + str(sum)

	return sum

digit_sum = calc_digit_sum( 2 ** 1000 )

print "ANSWER:" + str(digit_sum)
