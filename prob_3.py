'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

import itertools
import primes_util as util
from math import sqrt

#empirically, I think it'll be faster to just calculate the factors and THEN see which ones are primes...
def max_prime_factor(n):
	factors = [1]

	half = sqrt(int(n)) +1 #if we get here, we're too far ahead
	max_value = 1
	for i in itertools.count(3, 2): #no use in checking the pairs... I know they won't be primes
		if i >= half:
			break
		if n % i == 0 and i % 5 != 0 and util.is_prime(i): #let's trim a couple right now too...
			max_value = i
	return max_value

	
print max_prime_factor(600851475143)

