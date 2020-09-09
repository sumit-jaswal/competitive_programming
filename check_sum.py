# Find the numbers in an array that add upto a specific value and return true else return false.
# Input  : [4,7,1,-3,2], 6
# Output : ([4, 2], True)

def two_sum(list,k):
	sum = []
	for i in range(0,len(list)):
		for j in range(0,i):
			if(list[j]+list[i]==k):
				sum += [list[j]]
				sum += [list[i]]

	if(len(sum)!=0):
		return (sum,True)
	else:
		return False


print(two_sum([4,7,1,-3,2],6))