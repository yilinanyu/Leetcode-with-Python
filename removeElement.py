class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[tail] = nums[i]
                tail += 1
        return tail