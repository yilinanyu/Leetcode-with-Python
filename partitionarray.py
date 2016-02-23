class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        tail = 0
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i], nums[tail] = nums[tail] , nums[i]
                tail += 1
        return tail
