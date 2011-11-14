'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time

start = time.time()

def list_of_proper_divisors(n):
	divisors = [1]
	for i in range(2,n/2+1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def sum_of_divisors(n):
	return sum(list_of_proper_divisors(n))


def get_amicable(n):
	sum_of_d = sum_of_divisors(n)
	if sum_of_divisors(sum_of_d) == n  and sum_of_d !=n:
		return sum_of_d
	else:
		return 0

result = 0
for n in range(2, 10001):
	result += get_amicable(n)

print "Problem 21's answer is: {}.\nTook {} seconds to calculate.".format(result, time.time()-start) 
