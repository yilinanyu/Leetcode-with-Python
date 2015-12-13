class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                list = [0, 0]
                if A[left] == target: list[0] = left
                if A[right] == target: list[1] = right
                for i in range(mid, right+1):
                    if A[i] != target: list[1] = i - 1; break
                for i in range(mid, left-1, -1):
                    if A[i] != target: list[0] = i + 1; break
                return list
        return [-1, -1]