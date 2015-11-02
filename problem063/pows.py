#!/usr/bin/python
"""chicks' powers of 99 printer for Euler Project problem #63"""

import sys
import string
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

for pow in xrange(0,100):
	power = 99 ** pow
	digits = len(str(power))
	print "99^" + str(pow) + " == " + str(power) + " (" + str(digits) + " digits)"

