#!/usr/bin/python
"""chicks' answer to Euler Project problem #40"""

import sys
import string
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

champ = []
def build_champ(digits=0):
	n = 0
	while len(champ) < digits:
		add = map(int,list(str(n)))
#		if (n == 50):
#			print champ
#		if (n % 10000) == 0:
#			print n, add
		n = n + 1
		champ.extend(add)

build_champ(1000010)

print "champ[12]= " + str(champ[12])
#print "champ[1]= " + str(champ[1])
print "champ[10]= " + str(champ[10])
#print "champ[100]= " + str(champ[100])
#print "champ[1000]= " + str(champ[1000])

big_product=champ[1] * champ[10] * champ[100] * champ[1000] * champ[10000] * champ[100000] * champ[1000000]
answer = str(big_product)
print "ANSWER:" + answer
