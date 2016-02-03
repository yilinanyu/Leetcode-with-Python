class Solution(object):
    # title to number 
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        for i in range(l):
            res *= 26
            res += ord(s[i]) - 64
        return res
        # s = Solution()
        # print s.titleToNumber('Z')