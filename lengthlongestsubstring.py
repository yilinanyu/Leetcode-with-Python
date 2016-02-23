class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        head = 0
        res = 0
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[head])
                head += 1
            hashset.add(s[i])
            res = max(res, i-head + 1)
        return res if res <= len(s) else 0
        