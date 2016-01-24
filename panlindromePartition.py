class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
    
    def dfs(self, s, stringlist):
        if len(s) == 0: Solution.res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])
            
    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res