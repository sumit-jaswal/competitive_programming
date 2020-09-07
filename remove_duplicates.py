# Program to remove duplicates from a sorted array 

duplicates = [1,1,2,2,3,7,9,23,34,67,67,78,81,89,90,90,92,95,100,100,100]
print(duplicates, len(duplicates))

duplicates_removed = []
for i in range(0,len(duplicates)):
	if i == len(duplicates)-1:
		duplicates_removed.append(duplicates[i])
		break
	if duplicates[i] != duplicates[i+1]:
		duplicates_removed.append(duplicates[i])

print(duplicates_removed, len(duplicates_removed))