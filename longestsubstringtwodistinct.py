class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) <= 1:
            return len(s)
            
        j = -1
        start = ans = 0
        
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if j >= 0 and s[i] != s[j]:
                    start = j + 1
                j = i - 1
            ans = max(ans, i - start + 1)
        return ans