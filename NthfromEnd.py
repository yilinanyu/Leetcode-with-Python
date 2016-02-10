# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        dummy.next = head
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next
        