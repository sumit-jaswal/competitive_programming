# Move all zeroes in an array at the end of the array without changing the order of non zero digits.
# Input  : [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
# Output : [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

class Solution:
    def movezeroes(self,nums):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-i-1):
                if(nums[j]==0):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
           

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().movezeroes(nums)
print(nums)