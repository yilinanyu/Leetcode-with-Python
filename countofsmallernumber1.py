class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        # [1 2 5 7 8]
        A.sort()
        res = []
        for i in queries:
            l = 0 
            r = len(A) - 1
            while l < r:
                mid = l + (r - l) / 2
                if A[mid] >= i:
                    r = mid
                else:
                    l = mid + 1
            res.append(l)
            
        return res
            
        