class  solution(object):
	# """docstring for  solution"""
	# def __init__(self, arg):
	# 	super( solution, self).__init__()
	# 	self.arg = arg
	def numDecodings(self, s):
		n = len(s)
		if not s  or n == 0:
			return 0
		dp = [0] * (n + 1)
		dp[0] = 1
		# STORE  the number of two digits
		if int(s[0]) != 0:
			dp[1] = 1

		for i in range(2, n + 1):
			if int(s[i - 1]) != 0:
				dp[i] += dp[i - 1]
				two = int(s[i-2]) + s[i-1])
			if two>= 10 and two<= 26:
				dp[i] += dp[i-2]
		return dp[n]