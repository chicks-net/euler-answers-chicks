#!/usr/bin/python
"""chicks' answer to Euler Project problem #22"""

names_file = open("names.txt", "r")
line = names_file.readline()
quoted_names = line.split(",")

count = 1
accumulator = 0

names = []

for q in quoted_names:
	letters = list(q)
	remove_letters = 1
	if letters[-1] == "\n":
		remove_letters = 2
	new_name = ''.join(letters[1:0-remove_letters])
	names.append(new_name)

for name in sorted(names):
	letters = list(name)
	letters_score = 0
	for l in letters:
		letters_score = letters_score + ord(l) - ord('A') + 1
	name_score = count * letters_score
	#print " ".join([str(count),name,str(name_score)]);
	count = count + 1
	accumulator = accumulator + name_score

print "count=" + str(count)
print "ANSWER:" + str(accumulator)
