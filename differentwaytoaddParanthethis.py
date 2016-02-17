def diffWaystoCompute(input):
# #Hints:
# Divide and Conque.
# For each sign, divide into two parts for before and after it.
# Complexity:
# O(Catalan(n)) time
# O(1) space

	ans = []
	for i in range(len(input)):
		c = input[i]
		if c in "+-*":
			left = self.diffWaystoCompute(input[:i])
			right = self.diffWaystoCompute(input[i+1:])
			for m in left:
				for n in right:
					if c == "+":
						ans.append(m + n)
					elif c == "*":
						ans.append(m * n)
					elif c == "-":
						ans.append(m - n)
	if not ans:
		ans.append(int(input))
	return ans

