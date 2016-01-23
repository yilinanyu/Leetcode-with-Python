class Solution():
	def findFirstDuplicate(an):
		for i in an(0,len(an)-1):
			for j in an (i+1, len(an)-1):
				if an[i] == an[j]:
					return an[i]
				else:
					break
		return 
	findFirstDuplicate("aaaaaa")
