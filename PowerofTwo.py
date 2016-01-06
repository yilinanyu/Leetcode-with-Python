class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and not n&(n-1)
        # n & n - 1 removes the right most bit of n. 
        # If an integer is power of 2, there is a single bit in the binary representation of n. e.g. 
        # 16 = b1000, 
        # 16 - 1 = b0111, 
        # 16 & 16 - 1 = b1000 & b0111 = 0, 
        # 16 != 0, based on these facts there is only one bit in b1000, so 16 is power of 2.
        # 2 = 0010
        # 2-1 = 0001
        # 2 & 2-1 = 0010 & 0001 = 0000= 0 
        # 2 != 0
        # so 0 