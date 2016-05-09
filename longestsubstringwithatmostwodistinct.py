class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.defaultdict(int)
        res = 0
        head = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while len(dic) > 2:
                dic[s[head]] -= 1
                if dic[s[head]] == 0:
                    del dic[s[head]]
                head += 1
            res = max(res, i- head + 1)
        return res if res <= len(s) else 0
                
            