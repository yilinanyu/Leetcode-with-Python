class Solution(object):
    def removeElement(self, A, elem):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(A)-1
        for i in range(len(A) -1, -1, -1):
            if A[i] == elem:
                A[i],A[j] = A[j],A[i]
                j -= 1
        return j+1
        