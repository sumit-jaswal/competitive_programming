# Finding the index of a duplicate value in an sorted array.
# Return the output as a tuple such that the first digit is the starting index and the second digit is the last index of duplicte values.
# Input  : [1,2,2,2,2,3,4,7,8,8], 2
# Output : (1,4)

class Solution:
	def getRange(self,arr,target):
		value=[]
		count=0
		for var in arr:
			if(var==x):
				value+=[count]
			count+=1
		
		if(len(value)==0):
			return -1
		else:
			return (value[0],value[-1])


arr=[1,2,2,2,2,3,4,7,8,8]
x=2
print(Solution().getRange(arr,x))
