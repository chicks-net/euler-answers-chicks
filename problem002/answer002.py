#!/usr/bin/python

fibos = [ 1, 2 ]
last = 2
sum = 2

while last <= 4000000:
	last = fibos[-1] + fibos[-2]
	fibos.append(last)
	if ( (last % 2) == 0):
		sum += last

print "sum=" + str(sum)
