class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(len(A) / 2, -1, -1):
            self.sifeDown(i, A)
    
    def sifeDown(self, k, A):
        n = len(A)
        while k < n:
            minIndex = k
            if k * 2 + 1 < n and A[k * 2 + 1] < A[minIndex]:
                minIndex = k * 2 + 1
            
            if k * 2 + 2 < n and A[k * 2 + 2] < A[minIndex]:
                minIndex = k * 2 + 2
            
            if minIndex == k:
                return
            
            temp = A[minIndex]
            A[minIndex] = A[k]
            A[k] = temp
            
            k = minIndex