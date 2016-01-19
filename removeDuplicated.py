class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1

    A = [1,1,1,3]
    print removeDuplicates(A)
    print A