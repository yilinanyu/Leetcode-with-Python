class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        pre = 1; curr = 2
        while curr< len(nums):
            if nums[curr] == nums[pre] and nums[curr] == nums[pre-1]:
                curr+=1
            else:
                pre+=1
                nums[pre] = nums[curr]
                curr+=1
        return pre+1
        