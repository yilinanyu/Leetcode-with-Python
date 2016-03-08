class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # O(n^2) time 
        # O(n^2) space
        #dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        dp = [[1]*n for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        # last elment of the last element 
        return dp[-1][-1]