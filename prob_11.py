'''
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
- Grid has been placed in aux file
'''

f = open('prob_11_aux.txt')

line_list = f.readlines()
lines = []

for line in line_list:
	number_list = line.split()
	lines.append([int(x) for x in number_list])


def calculate_max_product():
	max_value = 0
	for i in range(0, len(lines)):
		for j in range(0, len(lines[0])):
			iteration_max = possible_val(lines, i, j)
			if iteration_max > max_value:
				max_value = iteration_max
	return max_value


def possible_val(matrix, x, y):
	local_max = 0
	limit_y = len(matrix)
	limit_x = len(matrix[0])
	#we need to check if there are enough positions in front of us
	count_forward = x <= limit_x-4
	count_downward = y <= limit_y-4
	count_up_right = count_forward and y-3 >= 0
	count_down_right = count_forward and count_downward
	
	if count_forward:	
		forward_value = matrix[x][y] * matrix[x+1][y] * matrix[x+2][y] * matrix[x+3][y]
		if forward_value > local_max:
			local_max = forward_value

	if count_downward:
		downward_value = matrix[x][y] * matrix[x][y+1] * matrix[x][y+2] * matrix[x][y+3]
		if downward_value > local_max:
			local_max = downward_value

	if count_up_right:	
		up_right_value =  matrix[x][y] * matrix[x+1][y-1] * matrix[x+2][y-2] * matrix[x+3][y-3]
		if up_right_value > local_max:
			local_max = up_right_value

	if count_down_right:		
		down_right_value =  matrix[x][y] * matrix[x+1][y+1] * matrix[x+2][y+2] * matrix[x+3][y+3]
		if down_right_value > local_max:
			local_max = down_right_value
	
	return local_max

print calculate_max_product()