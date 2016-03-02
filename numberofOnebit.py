
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        for i in range(32):
            if n & (0x00000001 << i) != 0:
                num += 1
            
        return num