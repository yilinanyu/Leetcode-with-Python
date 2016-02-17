# 解法II：时间复杂度O(n * log n)

# 二分查找（Binary Search）+ 鸽笼原理（Pigeonhole Principle）

# 参考维基百科关于鸽笼原理的词条链接：https://en.wikipedia.org/wiki/Pigeonhole_principle

# “不允许修改数组” 与 “常数空间复杂度”这两个限制条件意味着：禁止排序，并且不能使用Map等数据结构

# 小于O(n2)的运行时间复杂度可以联想到使用二分将其中的一个n化简为log n

# 参考LeetCode Discuss：https://leetcode.com/discuss/60830/python-solution-explanation-without-changing-input-array

# 二分枚举答案范围，使用鸽笼原理进行检验

# 根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

# 假设枚举的数字为 n / 2：

# 遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

# 否则可以确定解落在(n / 2, n]范围内。
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low