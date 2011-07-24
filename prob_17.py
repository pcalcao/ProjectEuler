'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

first_twenty_nol = {
	1 : 3,
	2 : 3,
	3 : 5,
	4 : 4,
	5 : 4,
	6 : 3, 
	7 : 5,
	8 : 5,
	9 : 4,
	10 : 3,
	11 : 6,
	12 : 6,
	13 : 8,
	14 : 8,
	15 : 7,
	16 : 7,
	17 : 9,
	18 : 8,
	19 : 8 
}

tens_nol = {
	20: 6,
	30: 6,
	40: 5,
	50: 5,
	60: 5,
	70: 7,
	80: 6, 
	90: 6
}



def number_of_letters(number):
	if number < 20: 
		return first_twenty_nol[number]
	
	if number < 100:
		converted = str(number)
		if number % 10 == 0:
			return tens_nol[number]
		else:
			return tens_nol[int(converted[0])*10] + number_of_letters(int(converted[1:]))
	if number < 1000:
		if number % 100 == 0: #100, 200, etc
			return first_twenty_nol[number / 100] + len('hundred')
		else:
			return first_twenty_nol[int(number / 100)] + len('hundred') + len('and') + number_of_letters(number % 100)
	
	greater_then_1000 = number_of_letters(int(number / 1000)) + len('thousand')
	if number % 1000 != 0:
		greater_then_1000 += len('and') + number_of_letters(number%1000)
	return greater_then_1000

	
import time

start = time.time()

result = sum( [number_of_letters(number) for number in range(1,1001)])

now = time.time()

print "Problem 17's answer is: {}.\nTook {} seconds to calculate.".format(result, now-start) 