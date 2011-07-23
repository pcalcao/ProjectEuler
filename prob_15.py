'''
Starting in the top left corner of a 2*2 grid, there are 6 routes (without backtracking) to the bottom right corner.
'''

import math, time

grid_side = 20

start = time.time()

#The answer to this problem lies with pascal triangle. If we map it to a grid, then the number in one of the positions is the number of paths from the 1x1 position to it.
#given that the number in a position of the pascal triangle can be obtained by using Combinatories, we have: 

result = math.factorial(2*grid_side)/(math.factorial(grid_side)*math.factorial(grid_side))

now = time.time()

print "Problem 15's answer is: {}.\nTook {} seconds to calculate.".format(result, now-start) 
