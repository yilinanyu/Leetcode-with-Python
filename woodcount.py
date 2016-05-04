class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    # [2,1,4] = 7 
    # [1,2,3,4,,,,,,114,,,,,,456]
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k: return 0
        l = 0
        r = max(L)
        while l < r:
            mid = l + (r - l + 1) / 2
            temp = sum([x / mid for x in L])
            if  temp >= k:
                l = mid
            else:
                r = mid - 1
        return r