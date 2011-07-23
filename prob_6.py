# -*- coding: utf-8 -*-  


'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

'''
The sum of the squares of the first n positive integers can be represented as (2n^3 + 3n^2 + n)/6
'''
def sum_of_squares(n):
	return (2*n**3 + 3*n**2 + n)/6

def square_of_sums(n):
	return (n*(n+1)/2)**2

print square_of_sums(100) - sum_of_squares(100)
