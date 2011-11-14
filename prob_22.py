'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

'''

import time

start = time.time()

name_file = open('names_prob_21.txt')
name_str = name_file.readline()

name_list = name_str.split(',')
name_list.sort()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def name_worth(name):
	worth = 0
	for i in range(0,len(name)):
		worth += alphabet.index(name[i])+1
	return worth


result = 0
for position,name in enumerate(name_list):
	result += (position+1)*name_worth(name)

print "Problem 22's answer is: {}.\nTook {} seconds to calculate.".format(result, time.time()-start) 