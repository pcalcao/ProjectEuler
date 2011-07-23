'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''

import time

start = time.time()


result = sum([int(x) for x in list(str(2**1000))])

now = time.time()

print "Problem 16's answer is: {}.\nTook {} seconds to calculate.".format(result, now-start) 