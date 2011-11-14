'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

def is_leap_year(n):
	return n % 4 == 0 and (n % 100 != 0 or n%400 == 0)

import time

start = time.time()

week_days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
monthly_days = [31,28,31,30,31,30,31,31,30,31,30,31]


def start_at_sunday_by_year(year_start, year_end, starting_at):
	sundays = 0
	if starting_at == 0:
		sundays += 1
	for year in range(year_start, year_end+1):
		for index, value in enumerate(monthly_days):
			if index == 1 and is_leap_year(year):
				value += 1
			day_difference = (value % 7)
			if week_days[(day_difference+starting_at)%7] == 'Sun':
				sundays += 1
			starting_at = (day_difference+starting_at)%7
	return sundays

result = start_at_sunday_by_year(1901,2000,2)

print "Problem 19's answer is: {}.\nTook {} seconds to calculate.".format(result, time.time()-start) 