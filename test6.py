class Solution:
    # @param an a string
    # @return n integer
    def reverseBits(an,n):
    	ab = an.replace(an[n-1], an[n-1] + '\n')
    	print ab
    reverseBits("aaaa",2)


