#!/usr/bin/python
"""chicks' answer to Euler Project problem #13"""

numbers_file = open("large_numbers.txt", "r")
lines = numbers_file.readlines()

accumulator = 0

for y in lines:
	accumulator = accumulator + int(y)
	#print "accumulator=" + str(accumulator)

str_sum = str(accumulator)
digits = str(len(str_sum))

print "sum digits=" + digits
print "sum=" + str_sum + ".00"

answer = "".join(list(str_sum)[:10])
print "left(sum,10)=" + answer
print "ANSWER:" + answer
