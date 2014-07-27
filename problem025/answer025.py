#!/usr/bin/python

fibos = [ 1, 1 ]
max_digits = 1

while max_digits < 1000:
	last = fibos[-1] + fibos[-2]
	fibos.append(last)
	digits = len(str(last))
	if digits > max_digits:
		max_digits = digits
		#print " ".join([str(last),"is the first fibonacci with",str(digits),"digits"])

# it wasn't clear to me if they wanted the place or the number itself
#print "ANSWER:" + str(last)
print "ANSWER:" + str(len(fibos))
