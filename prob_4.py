'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def is_palindrome(number):
	str_num = str(number)
	half_length = (len(str_num)/2)+1
	for i in range (0,half_length):
		first_idx = i
		second_idx = len(str_num)-(i+1)
		if first_idx == second_idx:
			return True
		first = str_num[first_idx]
		latest = str_num[second_idx]
		if first != latest:
			return False
	return True


#my first approach is O(n^2), I wonder how I could improve this...

max = 0
max_first_operand = 100
max_second_operand = 100
#If I could stop when I found the higher... that would be cool, not sure how I'd do that though, not trivial
for i in range (100,1000):
	for j in range(100, 1000):
		res = i*j
		if is_palindrome(res) and res > max:
			max = res
			max_first_operand = i
			max_second_operand = j

print "%d is the product of %d and %d" % (max, max_first_operand, max_second_operand)