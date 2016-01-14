class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    ##二分查找
# 由于有重复数字时，返回第一个出现的index，所以A[mid] == target时，end = mid
# 由于数组非常大，所以我们希望用一种方式找到刚刚好比target大一些的数作为end，代码如下：
# end = 0
# while end < len(A) and A[end] < target:
#   end = end * 2 + 1
# if end >= len(A):
#   end = len(A) - 1
  #
    def searchBigSortedArray(self, A, target):
        if not A:
            return -1

        end = 0
        while end < len(A) and A[end] < target:
            end = end * 2 + 1
        if end >= len(A):
            end = len(A) - 1

        start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end

        return -1