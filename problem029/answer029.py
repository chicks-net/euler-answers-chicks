#!/usr/bin/python
"""chicks' answer to Euler Project problem #29"""

import sys
import string
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

terms = {}

for a in xrange(2,101):
	for b in xrange(2,101):
#		print a,b
		term = a ** b
		if term in terms:
			terms[term] = terms[term] + 1
		else:
			terms[term] = 1


answer = str(len(terms))
print "ANSWER:" + answer
