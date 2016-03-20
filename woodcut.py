class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        
        maxLen = max(L)
        l, r = 1, maxLen
        
        while l < r:
            mid = l + (r - l + 1) / 2
            n = sum([p / mid for p in L])
            
            if n >= k:
                l = mid
            else:
                r = mid - 1
            
        return r/code>