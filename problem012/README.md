Euler Problem 12
================

* [Problem definition](http://projecteuler.net/problem=12)

Performance Analysis
--------------------

The naive implementation takes almost 8 hours:

	real	476m43.205s
	user	476m47.021s
	sys	0m3.277s

My first attempt at optimization took __x__ hours:

I've been trying to do this by hand and do it in python, but I'm considering using a library for the factorization to "cheat".
It looks like [Msieve](http://sourceforge.net/p/msieve/wiki/Home/) is a C library that does this fast and
[PySieve](https://github.com/dansefatale/PySieve) is a python wrapper for it.  But I haven't tried it yet.
