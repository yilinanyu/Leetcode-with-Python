# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        n = self.getLen(head)
        # incase k > n
        k = k % n
        if k == 0:
            return head
        #older head will be changed, so use dummy node and cur node = head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        # 先将cur 向前进k步,head 还在原地
        for i in range(k):
            cur = cur.next
        # 存在head 和 cur.next 所有head 和cur 都向前进
        while cur and cur.next:
            head = head.next
            cur = cur.next
        Newhead = head.next
        cur.next = dummy.next 
        head.next = None
        
        return Newhead
        
    def getLen(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n
        
        