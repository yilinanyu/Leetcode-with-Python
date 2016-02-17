def rotate(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n-k)
    reverse(nums, n-k, n)
    reverse(nums, 0, n)
def reverse(nums, start, end):
    for i in range(start, (start+end)/2):
        nums[i], nums[start + end - i - 1] = nums[start + end - i - 1], nums[i]
