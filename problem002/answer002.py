#!/usr/bin/python
"""chicks' answer to Euler Project problem #2"""

fibos = [1, 2]
last = 2
accumulator = 2

while last <= 4000000:
	last = fibos[-1] + fibos[-2]
	fibos.append(last)
	if (last % 2) == 0:
		accumulator += last

print "ANSWER:" + str(accumulator)
