# Checking whether parenthesis are balanced or not.
# Input  : {{{)))[]
# Output : False

class Solution:
	def isValid(self,s):
		dict_paren = {'(' : ')', '{' : '"}', '[' : ']'}
		print(dict_paren['('])
		count=0
		for paren in s:
			# if (paren=='{' or paren=='[' or paren=='('):
			if dict_paren[paren]:
				count += 1
				print("paren in", paren)
			if (paren=='}' or paren==']' or paren==')'):
				count -= 1
				print("paren out", paren)

		return (count==0)


s="{{{)))[]"
print(Solution().isValid(s))		