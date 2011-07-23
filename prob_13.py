'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

import time
ti = time.time()

file = open('prob_13_aux.txt', 'r')

number_list = [int(line) for line in file]
total = str(sum(number_list))

file.close()

print "Problem 13's answer is: {}.\nTook {} seconds to calculate.".format(total[:10], time.time() - ti)
