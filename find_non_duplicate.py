# Given a list of numbers, where every number shows up twice except for one number, find that one number.
# Input  : [4, 3, 2, 4, 1, 3, 2]
# Output : 1

def singleNumber(numbers_list):
	numbers_list_sorted = sorted(numbers_list)
	# Get the list containing all duplicates elements.
	duplicates = [numbers_list_sorted[x-1] for x in range(1,len(numbers_list_sorted)) if numbers_list_sorted[x-1]==numbers_list_sorted[x]]
	# Get the non duplicate element by comparing sorted list(numbers_list_sorted) and list with duplicate elements(duplicate)
	# and saving the uncommon element bewtween both the lists.
	non_duplicate = [str(x) for x in numbers_list_sorted if x not in duplicates]
	return ("".join(non_duplicate))

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))