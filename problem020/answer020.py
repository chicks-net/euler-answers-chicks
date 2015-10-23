#!/usr/bin/python
"""chicks' answer to Euler Project problem #20"""

import math

def calc_digit_sum(n):
	digits = list(str(n))
	sum = 0
	for digit in digits:
		sum += int(digit)

	#print str(n) + " -> " + str(sum)

	return sum

answer = calc_digit_sum( math.factorial(100) )

print "ANSWER:" + str(answer)
