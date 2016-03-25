class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        n = len(nums)
        if not nums or n < 2:
            return 0
        
        a = min(nums)
        b = max(nums)
        
        bucketSize = max(1, int((b - a - 1) // (n - 1)) + 1)
        bucketNumber = (b - a) // bucketSize + 1
        buckets = [None] * bucketNumber
        
        for i in nums:
            loc = (i - a) // bucketSize
            bucket = buckets[loc]
            
            if bucket is None:
                buckets[loc] = [i, i] # bucket = [minValue, maxValue]
            else:
                bucket[0] = min(bucket[0], i)
                bucket[1] = max(bucket[1], i)
        
        ans = 0
        x = 0
        while x < bucketNumber:
            if buckets[x] is None:
                x += 1
                continue
            y = x + 1
            while y < bucketNumber and buckets[y] is None:
                y += 1
            if y < bucketNumber:
                ans = max(ans, buckets[y][0] - buckets[x][1])
            x = y
        return ans