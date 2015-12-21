class Solution:
    # @param A, a list of integers
    # @return an integer
    # @a very subtle solution
    def firstMissingPositive(self, A):
        n=len(A)
        for i in range(n):
            if A[i]<=0: A[i]=n+2
        for i in range(n):
            if abs(A[i])<=n:
                curr=abs(A[i])-1
                A[curr]=-abs(A[curr])
        for i in range(n):
            if A[i]>0: return i+1
        return n+1