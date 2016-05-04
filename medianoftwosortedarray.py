class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 对于两个数列，寻找第k 个元素
        # 如果len 之和是奇数，求中间值；若为偶数，求两个中间值平均值
        n = len(nums1) + len(nums2)
        if n & 1:
            return self.kthnum(nums1, nums2, n/2)
        else:
            return (self.kthnum(nums1, nums2, n/2 - 1) + self.kthnum(nums1, nums2, n/2)) / 2.0
    # 对于两个数列，合并+ 取第k 值
    def kthnum(self, a, b, k):
        if len(a) == 0:
            return b[k]
        if len(b) == 0:
            return a[k]
        
        m = len(a) / 2
        n = len(b) / 2
        if k > m + n:
            if b[n] > a[m]:
                return self.kthnum(a[m + 1:], b, k - m - 1)
            else:
                return self.kthnum(a, b[ n + 1 :], k - n - 1)
        else:
            if b[n] > a[m]:
                return self.kthnum(a, b[:n], k)
                
            else:
                return self.kthnum(a[:m], b, k)
                
                
                
            
        
        
        