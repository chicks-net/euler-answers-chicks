#!/usr/bin/python
"""chicks' answer to Euler Project problem #34"""

import math

max_factor = 100

def calc_digit_factorial_sum(n):
	digits = list(str(n))
	sum = 0
	for digit in digits:
		sum += math.factorial( int(digit) )

	#print str(n) + " -> " + str(sum)

	return sum

for x in xrange(1,20000000):
	digit_sum = calc_digit_factorial_sum( x )

	if digit_sum == x:
		print str(x) + " -> " + str(digit_sum)

print "ANSWER:" + str(digit_sum)
