# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # return a linked list
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        #p1.next = None: 
        p2.next = p2.next.next
        return dummy.next
            