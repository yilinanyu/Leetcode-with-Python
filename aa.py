class Solution:
    #@param A a list of integers
    #@return an integer
    #huhsiuhid
    def trap(self, A):
        leftmosthigh = [0 for i in range(len(A))]
        leftmax = 0
        for i in range(len(A)):
            if A[i]> leftmax:
                leftmax = A[i]
            leftmosthigh[i] = leftmax
        rightmax= 0
        sum = 0
        for i in reversed(range(len(A))):
            if A[i] > rightmax:
                rightmax = A[i]
            if min(leftmosthigh[i],rightmax)-A[i]>0:
                sum += min(leftmosthigh[i],rightmax)-A[i]
        return sum

        