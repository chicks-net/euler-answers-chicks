#!/usr/bin/python
"""chicks' answer to Euler Project problem #17"""

def number_as_words(q):
	if q == 1:
		return "one"
	elif q == 2:
		return "two"
	elif q == 3:
		return "three"
	elif q == 4:
		return "four"
	elif q == 5:
		return "five"
	elif q == 6:
		return "six"
	elif q == 7:
		return "seven"
	elif q == 8:
		return "eight"
	elif q == 9:
		return "nine"
	elif q == 10:
		return "ten"
	elif q == 11:
		return "eleven"
	elif q == 12:
		return "twelve"
	elif q == 13:
		return "thirteen"
	elif q == 14:
		return "fourteen"
	elif q == 15:
		return "fifteen"
	elif q == 16:
		return "sixteen"
	elif q == 17:
		return "seventeen"
	elif q == 18:
		return "eighteen"
	elif q == 19:
		return "nineteen"
	elif q == 20:
		return "twenty"
	elif (q > 20 and q < 30):
		ones = int(list(str(q))[-1])
		return "twenty-" + number_as_words(ones) 
	elif q == 30:
		return "thirty"
	elif (q > 30 and q < 40):
		ones = int(list(str(q))[-1])
		return "thirty-" + number_as_words(ones) 
	elif q == 40:
		return "forty"
	elif (q > 40 and q < 50):
		ones = int(list(str(q))[-1])
		return "forty-" + number_as_words(ones) 
	elif q == 50:
		return "fifty"
	elif (q > 50 and q < 60):
		ones = int(list(str(q))[-1])
		return "fifty-" + number_as_words(ones) 
	elif q == 60:
		return "sixty"
	elif (q > 60 and q < 70):
		ones = int(list(str(q))[-1])
		return "sixty-" + number_as_words(ones) 
	elif q == 70:
		return "seventy"
	elif (q > 70 and q < 80):
		ones = int(list(str(q))[-1])
		return "seventy-" + number_as_words(ones) 
	elif q == 80:
		return "eighty"
	elif (q > 80 and q < 90):
		ones = int(list(str(q))[-1])
		return "eighty-" + number_as_words(ones) 
	elif q == 90:
		return "ninety"
	elif (q > 90 and q < 100):
		ones = int(list(str(q))[-1])
		return "ninety-" + number_as_words(ones) 
	elif q == 100:
		return "one hundred"
	elif (q > 100 and q < 200):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "one hundred and " + number_as_words(tens);
	elif q == 200:
		return "two hundred"
	elif (q > 200 and q < 300):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "two hundred and " + number_as_words(tens);
	elif q == 300:
		return "three hundred"
	elif (q > 300 and q < 400):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "three hundred and " + number_as_words(tens);
	elif q == 400:
		return "four hundred"
	elif (q > 400 and q < 500):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "four hundred and " + number_as_words(tens);
	elif q == 500:
		return "five hundred"
	elif (q > 500 and q < 600):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "five hundred and " + number_as_words(tens);
	elif q == 600:
		return "six hundred"
	elif (q > 600 and q < 700):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "six hundred and " + number_as_words(tens);
	elif q == 700:
		return "seven hundred"
	elif (q > 700 and q < 800):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "seven hundred and " + number_as_words(tens);
	elif q == 800:
		return "eight hundred"
	elif (q > 800 and q < 900):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "eight hundred and " + number_as_words(tens);
	elif q == 900:
		return "nine hundred"
	elif (q > 900 and q < 1000):
		tens = int(list(str(q))[-2])*10 + int(list(str(q))[-1])
		return "nine hundred and " + number_as_words(tens);
	elif q == 1000:
		return "one thousand"
	else:
		raise

def count_letters(n):
	words = number_as_words(n)
	words = words.translate(None, ' -')
	if n == 342:
		print "n=342: " + words + " " + str(len(words))
	return len(words)

total_count = 0;
for x in range(1,1001):
	letters = count_letters(x)
	total_count += letters
	print str(x) + " -> " + str(letters)


print "ANSWER:" + str(total_count)
