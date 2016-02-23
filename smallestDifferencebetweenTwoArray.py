class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        i = j = 0
        res = 2147483647
        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                res = min(A[i]- B[j], res)
                j += 1
            else:
                res = min(B[j]- A[i], res)
                i += 1
        return res
        