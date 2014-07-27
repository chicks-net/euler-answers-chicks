#!/usr/bin/python

input = open("large_numbers.txt","r")
lines = input.readlines()

sum = 0

for y in lines:
	sum = sum + int(y)
	#print "sum=" + str(sum)

str_sum = str(sum)
digits = str(len(str_sum))

print "sum digits=" + digits
print "sum=" + str_sum + ".00"
print "left(sum,10)=" + "".join(list(str_sum)[:10])
