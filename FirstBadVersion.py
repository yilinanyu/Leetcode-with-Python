#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right -left)/2
            if SVNRepo.isBadVersion(mid):
                right = mid -1
            else:
                left = mid + 1
        return left 
        
        