#!/usr/bin/python
"""chicks' answer to Euler Project problem #56"""

import math

max_digit_sum = 0

max_factor = 100

def calc_digit_sum(n):
	digits = list(str(n))
	sum = 0
	for digit in digits:
		sum += int(digit)

	#print str(n) + " -> " + str(sum)

	return sum

for a in range(1, max_factor):
	for b in range(1, max_factor):
		digit_sum = calc_digit_sum( a ** b )

		if digit_sum > max_digit_sum:
			max_digit_sum = digit_sum

print "ANSWER:" + str(max_digit_sum)
