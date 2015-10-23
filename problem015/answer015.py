#!/usr/bin/python
"""chicks' answer to Euler Project problem #15"""

import math

answer = 0
max_dim = 2
dim = 0

while dim < max_dim:
	add = 2 * (dim+1)
	answer += add
	print str(dim) + " " + str(add)
	dim = dim + 1

while dim > 2:
	add = 2 * (dim-1)
	answer += add
	print str(dim) + " " + str(add)
	dim = dim - 1

print "ANSWER:" + str(answer)
