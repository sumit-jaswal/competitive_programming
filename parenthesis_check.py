# Checking whether parenthesis are balanced or not.
# Input  : {{{))}(((}})[]
# Output : True

class Solution:
	def isValid(self,s):
		open_paren = ['(', '{', '[']
		close_paren = [')', '}', ']']
		in_paren = []
		out_paren = []

		if len(s)%2 != 0:
			return False
		else:
			for paren in s:
				if paren in open_paren:
					index_open = open_paren.index(paren)
					in_paren.append(index_open)
				if paren in close_paren:
					index_close = close_paren.index(paren)
					out_paren.append(index_close)
			return sorted(in_paren)==sorted(out_paren)

s="{{{))}(((}})[]"
print(Solution().isValid(s))		