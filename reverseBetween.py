# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = mPrev = ListNode(0)
        dummy.next = head
        # 先move mPrev 到mPrev
        for i in range(m - 1):
            mPrev = mPrev.next
        
        prev = mPrev.next
        cur = prev.next
        # reverse n - m 之间的list
        for i in range(n - m):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp 
        # 连接mprev 和 prev 与 cur    
        mPrev.next.next = cur
        mPrev.next = prev
        return dummy.next
        
        
        