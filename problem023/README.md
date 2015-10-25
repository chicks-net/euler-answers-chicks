# Euler Problem 23:  Non-abundant sums

[Problem Definition](https://projecteuler.net/problem=23):
> A perfect number is a number for which the sum of its proper divisors is exactly equal to
> the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14
> = 28, which means that 28 is a perfect number.
> 
> A number n is called deficient if the sum of its proper divisors is less than n and it is
> called abundant if this sum exceeds n.
> 
> As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can
> be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be
> shown that all integers greater than 28123 can be written as the sum of two abundant
> numbers. However, this upper limit cannot be reduced any further by analysis even though
> it is known that the greatest number that cannot be expressed as the sum of two abundant
> numbers is less than this limit.
> 
> Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

## Performance

On my VM this took:

	$ time ./answer023.pl 
	7428 abundant numbers found in 0.108746 seconds
	55175184 sums calculated for 57807 resultant sums in 66.821203 seconds
	crosscheck PASSed
	ANSWER:hahahaha

	real	1m7.007s
	user	1m6.131s
	sys	0m0.130s

While there could be some optimization in reducing the number of abundant numbers considered
the bulk of the slowness seems to be in the combinatorial library.
