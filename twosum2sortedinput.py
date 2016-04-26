class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or len(numbers) == 0:
            return []
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = l + (r - l)/2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] < target - numbers[i]:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
        