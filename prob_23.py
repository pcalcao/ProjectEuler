'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import euler_utility_methods as euler


def is_abundant(number):
	if number < 5391411025 and number % 2 != 0 and number % 3 != 0:
		return False
	return sum(euler.get_proper_divisors(number)) > number

def stupid_abundant_list(limit):
	return filter(lambda x: is_abundant(x) and x <= limit, xrange(1,limit))

def list_of_sums(limit, abundant_list):
	can_be_written_as_sum = {24}
	for i in range(24,limit):
		if i > 48 and i % 2 == 0: 
			can_be_written_as_sum.add(i) #every even number > 48 can be written as the sum of 2 abundant numbers
		for j in abundant_list:
			if j < i and is_abundant(i-j):
				can_be_written_as_sum.add(i)
				break
	return can_be_written_as_sum

import time

start = time.time()
abunda = stupid_abundant_list(20162)
#lista = list_of_sums(20162, abunda)
def is_sum_of_abundant(number, abundant_list):
	return any(number-i for i in abundant_list if number-i in abundant_list)

result = (20161**2+20161)/2 - sum([x for x in range(1,20162) if is_sum_of_abundant(x, abunda)])


print result
print "took {} secs".format(time.time()-start)