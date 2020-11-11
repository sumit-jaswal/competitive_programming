# You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

# Input  : [2, 3, 7, 6, 8, -1, -10, 15]
# Output : 1
# Output is 1 because it is the smallest positive integer that doesn't exist in the array.


def first_missing_positive(nums):
	positive_numbers = [n for n in sorted(nums) if n>0]
	missing_numbers = [i for i in range(1, positive_numbers[-1]) if i not in positive_numbers]
	return missing_numbers[0]

print(first_missing_positive([2, 3, 7, 6, 8, -1, -10, 15]))