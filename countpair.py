class CountPairs(object):
	def countPairs(num, target): # define a nil dictionary
		dict = {}
		count = 0
		for i in xrange(len(num)):
			x = num[i]
			if target-x in dict:
			count +=1 
			else:
				dict[x]=i 
		return count