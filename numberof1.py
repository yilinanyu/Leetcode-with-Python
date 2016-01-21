class Solution:
    # @param a list of integers
    # @return an integer
    def NumberofOne(n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans