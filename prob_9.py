'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
from math import sqrt

n = 25
print n*15+n*8+n*17

def generate_triplet(m, n):
	a = 2*m*n
	b = n**2-m**2
	c = n**2 + m**2
	return (a,b,c)

upper_limit = int(sqrt(1000))
for m in range(1, upper_limit):
	for n in range(m+1, upper_limit):
		triplet = generate_triplet(m,n)
		if 1000 == (triplet[0]+triplet[1]+triplet[2]):
			print 'found triplet with n:%d m%d at: ' %(n,m)
			print triplet
			print 'product is : %d' % (triplet[0]*triplet[1]*triplet[2])
			break
		if 1000 % (triplet[0]+triplet[1]+triplet[2]) == 0:
			print 'found candidate at: ' 
			print triplet