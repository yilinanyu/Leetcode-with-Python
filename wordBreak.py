class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #The idea is the following:d is an array that contains booleans
        #d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word
        #Example:s = "leetcode"words = ["leet", "code"]
        # d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
        # d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
        # Dynamic Programming
        # dp(i) = dp(j) && s[j, i) in dict, 0 <= j < i
        # O(n^2) time
        # O(n) space

        n = len(s)
        if n == 0 or not s:
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            # every substring
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        #last value
        return dp[-1] 

        