#!/usr/bin/python

possible_factors = [ ]

for z in range(10,100):
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
