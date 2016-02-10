# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # head 1 and head 2 
        h1 = cur1 = ListNode(0)
        h2 = cur2 = ListNode(0)
        while head:
            tmp = head.next
            if head.val < x:
                cur1.next = head
                head.next = None
                cur1 = cur1.next
            else:
                cur2.next = head
                head.next = None
                cur2 = cur2.next
            head = tmp 
        cur1.next = h2.next 
        return h1.next 
        