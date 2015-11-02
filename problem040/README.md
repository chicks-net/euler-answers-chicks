# Euler Problem 40: Champernowne's constant

[Problem Definition](https://projecteuler.net/problem=40):
> An irrational decimal fraction is created by concatenating the positive integers:
>
>            0.123456789101112131415161718192021...
>
> It can be seen that the 12^th digit of the fractional part is 1.
>
> If `d[n]` represents the n^th digit of the fractional part, find the value of the following expression.
>
>                           d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]

## Commentary

The problems statement does not clarify if *n* is 0-based or 1-based.  Many programmers would
assume 0-based which leads to `d[10]=0` and so the product would also be 0.  Since the Euler
site doesn't accept 0 we are left hoping that *n* is 1-based.  Luckily that path lead to
an acceptable answer.
