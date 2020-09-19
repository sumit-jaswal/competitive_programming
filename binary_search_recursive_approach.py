# Binary Search
# Searching for an element in a sorted list by dividing it into sublists based on the location of the element to be found.   '''
# Recursive approach

def binary_search_recursive(list1,element,lower,higher):
	global found
	found = 0
	if(lower<=higher):
		half = (lower+higher)//2
		if (element<list1[half]):
			binary_search_recursive(list1, element, lower, half-1)
		elif (element>list1[half]):
			binary_search_recursive(list1, element, half+1, higher)
		else:
			found = 1
	if found:
		return True
	else:
		return False

list1 = [232,453,673,894,1236,3237,5788]
element = 894
print(binary_search_recursive(list1, element, 0, len(list1)))