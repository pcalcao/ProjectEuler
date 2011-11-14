def summation(n):
	return (n**2+n)/2

from math import sqrt

def get_proper_divisors(number):
	proper_divisors = {1}
	for i in range(2, int(sqrt(number))+1):
		if number % i == 0:
			proper_divisors.add(i)
		divisor = number/i
		if number%divisor == 0 and divisor < number:
			proper_divisors.add(divisor)
	return proper_divisors	