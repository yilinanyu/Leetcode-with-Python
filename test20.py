class Solution:
	def sqrt(x):
		res = 0
		while res**2 <= x:
			if res **2 == x:
				return res
			else:
				res += 1
	print sqrt(16)

		
