'''
PROBLEM N. 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Greatest common divisior using the Euclidean Algorithm, vide http://en.wikipedia.org/wiki/Euclidean_algorithm
'''
def gcd(a, b):
	if a == b:
		return a
	if a == 0:
		return b
	if b == 0:
		return a
	if a > b:
		remainder = a%b
		return gcd(remainder, b)
	if b > a:
		remainder = b%a
		return gcd(remainder, a)


'''
Lowest common denominator, using: 
lcd(a,b) = |a*b|/gcd(a,b)
'''
def lcd(a, b):
	return a*b/gcd(a,b)

print reduce(lcd, range(1,21))