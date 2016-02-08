# 解题思路：这道题是很有名的编辑距离问题。用动态规划来解决。状态转移方程是这样的：
# dp[i][j]表示word1[0...i-1]到word2[0...j-1]的编辑距离。
# 而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。
# 同理dp[0][i]也是如此，等于i，因为只需做i次插入操作就可以了。
# dp[i-1][j]变到dp[i][j]需要加1，因为word1[0...i-2]到word2[0...j-1]的距离是dp[i-1][j]，
# 而word1[0...i-1]到word1[0...i-2]需要执行一次删除，
# 所以dp[i][j]=dp[i-1][j]+1；
# 同理dp[i][j]=dp[i][j-1]+1，
# 因为还需要加一次word2的插入操作。
# 如果word[i-1]==word[j-1]，则dp[i][j]=dp[i-1][j-1]，
# 如果word[i-1]!=word[j-1]，那么需要执行一次替换replace操作，所以dp[i][j]=dp[i-1][j-1]+1，以上就是状态转移方程的推导。
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m=len(word1)+1; n=len(word2)+1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i]=i
        for i in range(m):
            dp[i][0]=i
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
        return dp[m-1][n-1]