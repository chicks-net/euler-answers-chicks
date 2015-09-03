#!/usr/bin/python
"""chicks' answer to Euler Project problem #3"""

def factor(n):
	factors = []
	x = 2
	while x < n:
		if n % x == 0:
			factors.append(x)
		if (x % 10000000) == 0:
			print "\tchecking " + str(x) + " for " + str(n) + " (" + str(float(x/n)) + "%)"
		x = x + 1

	print str(n) + " has " + str(len(factors)) + " factors"

	return factors

def prime_factor(n):
	any_factors = factor(n)
	prime_factors = []
	for x in any_factors:
		x_factors = factor(x)
		if len(x_factors) == 0:
			prime_factors.append(x)

	return prime_factors

print "prime factors of 13195 are " + str(prime_factor(13195))
print "prime factors of 131950 are " + str(prime_factor(131950))
print "prime factors of 600851475143 are " + str(prime_factor(600851475143))
