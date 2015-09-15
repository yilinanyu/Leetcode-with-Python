class Solution:
    def uniquePaths(self, m, n):
       if n==1 and m==1:
          dp = [[1]]
       elif n==1 and m >1:
          dp = [[1] for j in range(m)]
       elif m ==1 and n >1:
          dp = [[1 for i in range(n)]]
       else:
          dp = [[0 for i in range(n)] for j in range(m)]
          for i in range(0,n):
              dp[0][i] = 1
          for i in range(0,m):
              dp[i][0] = 1
          for i in range(1,m):
              for j in range(1,n):
                  dp[i][j] = dp[i-1][j]+dp[i][j-1]
       return dp[m-1][n-1]
        