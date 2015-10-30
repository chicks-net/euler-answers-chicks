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
	elif j >= grid_rows or k >= grid_cols :
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
grid_rows = len(grid)
grid_cols = len(grid[0])

for z in range(0,grid_rows):
	row = grid[z]
	pp.pprint(row)

	for y in range(0,len(row)):
		# back diaganol
		product = gg(z,y) * gg(z-1,y-1) * gg(z-2,y-2) * gg(z-3,y-3)
		coord = ( "(" + str(z) + "," + str(y) + ") " + 
			",".join(map(str,(gg(z,y),gg(z-1,y-1),gg(z-2,y-2),gg(z-3,y-3))))
		)
		print coord + " \> " + str(product)
		if product > big_product:
			big_product = product
			big_coord = coord

		# forward diaganol
		product = gg(z,y) * gg(z+1,y+1) * gg(z+2,y+2) * gg(z+3,y+3)
		coord = ( "(" + str(z) + "," + str(y) + ") " + 
			",".join(map(str,(gg(z,y),gg(z+1,y+1),gg(z+2,y+2),gg(z+3,y+3))))
		)
		print coord + " /> " + str(product)
		if product > big_product:
			big_product = product
			big_coord = coord

		# left-right
		product = gg(z,y) * gg(z+1,y) * gg(z+2,y) * gg(z+3,y)
		coord = ( "(" + str(z) + "," + str(y) + ") " + 
			",".join(map(str,(gg(z,y),gg(z+1,y),gg(z+2,y),gg(z+3,y))))
		)
		print coord + " -> " + str(product)
		if product > big_product:
			big_product = product
			big_coord = coord

		# up-down
		product = gg(z,y) * gg(z,y+1) * gg(z,y+2) * gg(z,y+3)
		coord = ( "(" + str(z) + "," + str(y) + ") " + 
			",".join(map(str,(gg(z,y),gg(z,y+1),gg(z,y+2),gg(z,y+3))))
		)
		print coord + " |> " + str(product)
		if product > big_product:
			big_product = product
			big_coord = coord


answer = str(big_product)
print "coord:" + big_coord
print "ANSWER:" + answer
