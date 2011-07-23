'''Find the sum of all the multiples of 3 or 5 below 1000.'''

'''
We could simply brute force this and it would be fast enough... but let's use summation to solve it, kk?

http://en.wikipedia.org/wiki/Summation

since Sum(1..n) = (n^2+n)/2, we can do this without iterating over the numbers, just some simple calculations, thanks to http://mathworld.wolfram.com/FaulhabersFormula.html
'''
import itertools

def summation(n):
	return (n**2+n)/2

#we want the multiples of 3 + the multiples of 5, but we need to subtract the commons (multiples of 15) since we added those twice.
print 3*summation(999/3) + 5*summation(999/5) - 15*summation(999/15)


