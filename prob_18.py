'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
...

This simple code solves both problem 18 and problem 67. 
They're exactly the same problem, only problem 18 _could_ be solved through brute forcing all paths while for number 67 you actually had to come up with a good solution.
Just switch the files that are read at the begining, and you'll have your answers!

'''

#f = open('prob_18_aux.txt')
f = open('prob_67_aux.txt')

pyramid = [[int(x) for x in line.split()] for line in f.readlines()]

import time

start = time.time()

for i in range(len(pyramid)-2, -1,-1):
	line = pyramid[i]
	bottom = pyramid[i+1]
	for line_index in range(0,len(line)):
		right = bottom[line_index+1] #the bottom number to the right
		left = bottom[line_index]
		pyramid[i][line_index] += max(right,left)

result = format(pyramid[0][0])

print "Problem 18's answer is: {}.\nTook {} seconds to calculate.".format(result, time.time()-start) 
