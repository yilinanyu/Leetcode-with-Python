class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #使用两个"指针"x和y，初始令y = 0 利用x遍历数组nums：若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

        #算法简析：y指针指向首个0元素可能存在的位置,遍历过程中，算法确保[y, x)范围内的元素均为0
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y],nums[x]
                y += 1