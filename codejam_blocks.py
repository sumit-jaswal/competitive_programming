# Google Codejam Question
# Find the area of the largest rectangle formed by buliding blocks of some width and height.
# The blocks are placed next to each other such that there is no gap between any two consecutive blocks. 
# Input  : n - Number of blocks
# 		 : w,h - width of block, height of block
# Outupt : o - area of largest rectangle formed by these blocks.

block_count = int(input('Enter the total count of blocks : '))
width=[]
height=[]

for i in range(0, block_count):
	vara, varb = map(int, input("Enter width & height of block seperated by comma : ").split(','))
	width += [vara]
	height += [varb]

total_width=0
for i in width:
	total_width=total_width+i

min_height = sorted(height)[0]
print('Total area of blocks is : ', (total_width*min_height), ' square units')