#!/usr/bin/python


def collatz(n,verbose=False):
	len = 1 # start with 1 to account for not counting the final "1"

	while n > 1:
		len += 1
		if verbose:
			print str(n) + ",",
		if (n % 2) == 0:
			n = n / 2
		else:
			n = (3 * n) + 1 

	if verbose:
		print "1"

	return len

check_n = 1
max_len = 0
max_n = 0

while check_n < 1000000:
	this_len = collatz(check_n)
	if this_len > max_len:
		max_len = this_len
		max_n = check_n

	if (check_n % 10000) == 0:
		perc = check_n / 1000000.0
		print str(perc*100) + "% done: max_len=" + str(max_len) + " max_n=" + str(max_n)

	check_n += 1

collatz(max_n,True)
print "ANSWER:" + str(max_n)
#print "max_len=" + str(max_len)
