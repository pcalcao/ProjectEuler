'''
n! means n * (n - 1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ...* 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
'''

import math, time

start = time.time()

fact = str(math.factorial(100))

result = 0
for pos in range(0, len(fact)):
	result+= int(fact[pos])

print "Problem 20's answer is: {}.\nTook {} seconds to calculate.".format(result, time.time()-start) 
