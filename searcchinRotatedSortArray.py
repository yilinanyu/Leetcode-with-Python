class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[mid] >= A[left]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1