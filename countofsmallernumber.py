class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A.sort()
        ans = []
        
        for q in queries:
            ans.append(self.bSearch(A, q))
        
        return ans
    
    def bSearch(self, A, q):
        l, r = 0, len(A) - 1
        
        while l < r:
            mid = l + (r - l) / 2
            if A[mid] >= q:
                r = mid
            else:
                l = mid + 1
        
        return l