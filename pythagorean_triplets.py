# Check whether an array contains Pythagorean Triplets
# Pythagorean Triplets are 3 numbers which follow Pythagoras Theoram Forlmual i.e. a**2 = b**2 + c**2
# Input  : [3,12,5,4,13],13)
# Output : ([12, 5], True)
# Explanation : 12**2 + 5**2 = 13**2 i.e. 144 + 25 = 169

def pythagorean_triplets(lis,k):
	sum = []
	for i in range(0,len(lis)):
		for j in range(0,i):
			if(lis[i]**2 + lis[j]**2 == k**2):
				sum += [lis[j]]
				sum += [lis[i]]
				return (sum,True)

print(pythagorean_triplets([3,12,5,4,13],13))