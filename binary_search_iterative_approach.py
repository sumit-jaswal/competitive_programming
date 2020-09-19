# Binary Search
# Searching for an element in a sorted list by dividing it into sublists based on the location of the element to be found
# Iterative approach
	
def binary_search_iterative(array,search):
	lower = 0
	higher = len(array)
	while(lower<=higher):
		half = (lower+higher)//2
		if(search>array[half]):
			lower = half+1
		elif(search<array[half]):
			higher = half-1
		else:
			return True
	return False

array = [23,45,67,89,123,323,578]
search = 67
print(binary_search_iterative(array,search))