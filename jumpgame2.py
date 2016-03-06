class Solution:
    # @param A, a list of integers
    # @return an integer
    # def jump(self, A):
    #     maxint = 1<<31 - 1
    #     dp = [ maxint for i in range(len(A)) ]
    #     dp[0] = 0
    #     for i in range(1, len(A)):
    #         for j in range(i):
    #             if A[j] >= (i - j):
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #     return dp[len(A) - 1]
    # dp is time limited exceeded!
    
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.
    def jump(self, A):    
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret