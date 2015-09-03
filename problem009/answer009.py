#!/usr/bin/python
"""chicks' answer to Euler Project problem #9"""

import math

product_abc = 1

for a in range(1, 500):
	b = a + 1
	c = math.sqrt(a ** 2 + b ** 2)

	while (a + b + c) < 1001:
		b += 1
		c = math.sqrt(a ** 2 + b ** 2)
		#print "a=" + str(a) + " b=" + str(b) +  " c=" + str(c)
		if (a + b + c) == 1000:
			print "a=" + str(a) + " b=" + str(b) +  " c=" + str(c)
			print "a+b+c=" + str(a+b+c) + " b^2=" + str(b**2) +  " c^2=" + str(c**2)
			product_abc = int(a * b * c)
			break

print "ANSWER:" + str(product_abc)
