'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import primes_util

print reduce(lambda x,y: x+y, primes_util.erastot_sieve(2000000))