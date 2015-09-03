#!/usr/bin/python
"""chicks' answer to Euler Project problem #4"""

possible_factors = []

for z in range(100, 1000):
	possible_factors.append(z)

max_product = 0
max_x = 0
max_y = 0

for y in possible_factors:
	for x in possible_factors:
		product = x * y
		#print str(product) + " = " + str(x) + " * " + str(y)
		digits = list(str(product))
		backwards = list(digits)
		backwards.reverse()
		#print product, digits, backwards
		if digits == backwards:
			#print str(product) + " = " + str(x) + " * " + str(y)

			if product > max_product:
				max_product = product
				max_x = x
				max_y = y

print str(max_product) + " = " + str(max_x) + " * " + str(max_y)
print "ANSWER:" + str(max_product)
