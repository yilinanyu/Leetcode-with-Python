class Solution(object):
    def search(self, nums, target):
        left = 0; right = len(nums)-1
        while left<=right:
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            if nums[mid]>=nums[left]:
                if target< nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left= mid+1
            elif nums[mid]<= nums[left]:
                if target> nums[mid] and target <= nums[right]:
                    left = mid+1
                else: 
                    right = mid-1
        return -1
        