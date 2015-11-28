#!/usr/bin/python
"""chicks' answer to Euler Project problem #18"""

import sys
import string
import re
import pprint

# read command line
argcount = len(sys.argv)
if argcount <= 1:
	raise ValueError("missing filename on command line")
triangle_filename = sys.argv[1]
print str(argcount) + " arguments: " + triangle_filename 

# read file
with open(triangle_filename, "r") as triangle_file:
	lines = triangle_file.readlines()
	print str(len(lines)) + " lines read"

triangle = []
for y in lines:
	y = string.strip(y)
	fields = re.split('\s+', y)
	int_fields = []
	for f in fields:
		int_fields.append(int(f))
	triangle.insert(0,int_fields)
	c = len(fields)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(triangle)

rows = len(triangle) - 1
for z in range(0,rows):
	row = triangle[z]
	pp.pprint(row)

	entries = len(row) - 1
	for y in range(0,entries):
		a = row[y]
		b = row[y + 1]
		#print "comparing " + str(a) + " and " + str(b)
		adder = 0
		if a >= b:
			adder = a
		else:
			adder = b

		triangle[z + 1][y] += adder


answer = str(triangle[rows][0])
print "ANSWER:" + answer
