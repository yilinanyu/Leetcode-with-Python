
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = 0
        
        for i in range(32):
            a |= ((n >> i) & 1) << (31 - i)
        
        return a