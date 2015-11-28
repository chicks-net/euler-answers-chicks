#!/usr/bin/python
"""chicks' answer to Euler Project problem #1"""

accumulator = 0
for n in xrange(1, 1000):
	if (n % 3) == 0 or (n % 5) == 0:
		accumulator += n

print "ANSWER:" + str(accumulator)
