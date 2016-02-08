class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        if S is None or len(S) == 0:
            return 0
        S.sort()
        res = 0
        
        for i in range(len(S)):
            l = 0
            r = i - 1
            while l < r:
                if S[l] + S[r] > S[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        
        return res