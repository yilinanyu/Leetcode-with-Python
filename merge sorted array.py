class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        tmp = [0 for i in range(m + n)]
        i = 0; j = 0; k = 0
    #for normal situation, just compare and get the larger one to the temp array
        while i < m and j < n:
            if A[i] <= B[j]:
                tmp[k] = A[i]; i += 1
            else:
                tmp[k] = B[j]; j += 1
            k += 1
    #edge situation: if i equals to the edge and k not full, just pull all B array into the temp array
        if i == m:
            while k < m + n:
                tmp[k] = B[j]; k += 1; j += 1
        if j == n:
            while k < m + n:
                tmp[k] = A[i]; i += 1; k += 1
    # pull the temp [i] to the array A 
        for i in range(0, m + n):
            A[i] = tmp[i]