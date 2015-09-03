#!/usr/bin/python
"""chicks' answer to Euler Project problem #12"""

def factor(n):
	factors = [1]
	x = 2
	while x <= n:
		if n % x == 0:
			factors.append(x)
		if (x % 10000000) == 0:
			print "\tchecking " + str(x) + " for " + str(n) + " (" + str(float(x)/n) + "%)"
		x = x + 1

#	print str(n) + " has " + str(len(factors)) + " factors"

	return len(factors)

max_divisors = 0
n = 0
triangle = 0

while max_divisors < 502:
	n += 1
	loop_n = n
	triangle = 0
	while loop_n:
		triangle += loop_n
		loop_n -= 1
	divisors = factor(triangle)

	if divisors > max_divisors:
		max_divisors = divisors
		print "n=" + str(n) + " triangle " + str(triangle) + " has " + str(max_divisors) + " divisors"


print "ANSWER:" + str(triangle)
