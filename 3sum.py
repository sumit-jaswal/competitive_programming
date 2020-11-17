# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. 
# Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

# Input  : nums = [0, -1, 2, -3, 1]
# Output : [0, -1, 1], [2, -3, 1]

class Solution(object):
  def threeSum(self, nums):
    from itertools import combinations
    is3 = []
    for positions in combinations(nums, 3):
        if positions[0] + positions[1] + positions[2] is 0:
            is3 += [[positions[0], positions[1], positions[2]]]
    return is3

nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
