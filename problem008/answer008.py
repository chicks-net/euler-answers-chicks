#!/usr/bin/python

digits = [ ]

input = open("1000digit.txt","r")
lines = input.readlines()

for line in lines:
	line = line.rstrip()
	letters = list(line)
	for letter in letters:
		digits.append(int(letter))

#print "digits has " + str(len(digits)) + " elements"

greatest=0

for place in range(1000-13+1):
	start = 1
	mydigits = [ ]
	for member in range(13):
		digit = digits[place+member]
		mydigits.append(digit)
		start *= digit
		#print "place=" + str(place) + " start=" + str(start) + " digit=" + str(digit)

	#print "place=" + str(place) + " mydigits=" + str(mydigits) + " start=" + str(start)

	if start > greatest:
		greatest = start

print "ANSWER:" + str(greatest)
