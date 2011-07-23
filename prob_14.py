'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

'''
First approach:
'''

def collatz_num (n):
	if n % 2 == 0: 
		return n/2	
	else:
		return n*3+1

def collatz(n):	
	total = 1
	while n>1:
		n=collatz_num(n) 
		total +=1
	return total

'''
And now with some memoization in the mix:
'''
collatz_map = {1:1}

def recursive_collatz(n):
	if n in collatz_map:
		return collatz_map[n]
	if n % 2 == 0:
		x = 1 + recursive_collatz(int(n/2))
	else:
		x = 1 + recursive_collatz(int(3*n+1))
	collatz_map[n] = x
	return x

import time

start_time = time.time()

maior = 0
numero = 1

for i in range(5, 1000000):
	temp = recursive_collatz(i)
	if temp > maior: 
		numero = i
		maior = temp

print "Problem 14's answer is: {}.\nTook {} seconds to calculate.".format(numero, time.time() - start_time)
