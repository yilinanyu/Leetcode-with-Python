class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = dict()
        for x in range(len(nums)):
            idx = numDict.get(nums[x])
            if idx >= 0 and x-idx <= k:
                return True
            numDict[nums[x]] = x
        return False