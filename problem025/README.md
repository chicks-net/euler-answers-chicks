Euler Problem 25
================

Faster than not found
---------------------

I'm not making this up:

	chicks@silver 16:55:18 problem025 !2031 $ time answer025.py 
	answer025.py: command not found

	real	0m0.134s
	user	0m0.092s
	sys	0m0.017s
	chicks@silver 16:56:12 problem025 !2032 $ time ./answer025.py 
	ANSWER:4782

	real	0m0.033s
	user	0m0.025s
	sys	0m0.007s

So in real time it took a quarter of the time to calculate the fibonacci sequence
up to 1000 digits than it did to produce a command not found message.  Once things
are cached the `command not found` does improve, but not enough to be faster than
the fibonacci calculation:

	chicks@silver 16:59:45 problem025 !2052 $ time answer025.py 
	answer025.py: command not found

	real	0m0.080s
	user	0m0.063s
	sys	0m0.016s

So it still takes 2.4 times as long to produce the `commad not found` error
than it takes to load python, parse the script, and add 4780 numbers.

Maybe I've found something that python is highly performant with.

Grump
-----

The definition of the fibonacci sequence is off-by-one from the definition in problem 2.

