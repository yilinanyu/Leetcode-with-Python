class Solution:
    def compare_strings(self, A, B):
        m = len(A)
        n = len(B)
        if n == 0:
            return True
        if n > m:
             return False
        for i in range(m-n+1):
            for j in range(n):
                if A[i+j] != B[j]:
                    break
                else:
                    if j == n - 1:
                        return True
        return False
        