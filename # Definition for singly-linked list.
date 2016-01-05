# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        #p 和 tmp 的利用
        p = dummy 
        tmp = dummy.next
        while p.next:
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if tmp == p.next:
                p = p.next
                tmp = p.next
            else:
                p.next = tmp.next
        return dummy.next