class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # @good coding!
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]