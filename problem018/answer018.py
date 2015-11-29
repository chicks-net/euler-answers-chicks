#!/usr/bin/python
"""chicks' answer to Euler Project problem #18/67"""

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
for line in lines:
	fields = line.strip().split()
	int_fields = [int(f) for f in fields]
	triangle.insert(0, int_fields)

pretty = pprint.PrettyPrinter(indent=4)
#pretty.pprint(triangle)

rows = len(triangle) - 1
for z, row in enumerate(triangle):
	pretty.pprint(row)

	entries = len(row) - 1
	for y in range(0, entries):
		triangle[z + 1][y] += max(row[y], row[y + 1])


answer = str(triangle[rows][0])
print "ANSWER:" + answer
