#!/usr/bin/python
"""chicks' answer to Euler Project problem #11"""

import sys
import string
import re
import pprint

# read file
grid_filename = '20-20.txt'
grid_file = open(grid_filename, "r")
lines = grid_file.readlines()
print str(len(lines)) + " lines read"

pp = pprint.PrettyPrinter(indent=4)
grid = []

def gg(j,k):
	if j<0 or k<0:
		return 1
	else:
		return grid[j][k]

for a in lines:
	a = string.strip(a)
	fields = re.split('\s+', a)
	int_fields = []
	for f in fields:
		int_fields.append(int(f))
	grid.append(int_fields)

#pp.pprint(grid)

big_product = 0
big_coord = ""
rows = len(grid)
for z in range(0,rows):
	row = grid[z]
	pp.pprint(row)

	for y in range(0,len(row)):
		product = gg(z,y) * gg(z-1,y-1) * gg(z-2,y-2) * gg(z-3,y-3)
		coord = "(" + str(z) + "," + str(y) + ")"
		print coord + " -> " + str(product)
		if product > big_product:
			big_product = product
			big_coord = coord


answer = str(big_product)
print "coord:" + big_coord
print "ANSWER:" + answer
