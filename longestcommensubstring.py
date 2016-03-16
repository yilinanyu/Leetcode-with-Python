class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                l = 0
                while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
                    l += 1
                if l > ans:
                    ans = l
        return ans
        
                        
                