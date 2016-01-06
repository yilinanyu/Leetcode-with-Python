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
        #考虑eage case： 当k >> len(list):so we firstly need to count the lengh of list then move k%count places
        if k == 0:
            return head
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - (k % count)
        for i in range(0,step):
            p = p.next
        head = p.next
        p.next = None
        return head
        