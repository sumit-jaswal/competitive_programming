# Checking whether parenthesis are balanced or not.

class Solution:
	def isValid(self,s):
		count=0
		for paren in s:
			if (paren=='{' or paren=='[' or paren=='('):
				count += 1
			if (paren=='}' or paren==']' or paren==')'):
				count -= 1

		return (count==0)


s="{{{)))[]"
print(Solution().isValid(s))		