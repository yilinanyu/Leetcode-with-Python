# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or not head.next:
            return head
        
        l = self.getLen(head)
        n = l / k
        dummy = cur = ListNode(0)
        dummy.next = head
        
        for i in range(n):
            pre = None
            start = head
            for i in range(k):
                tmp = head.next
                head.next = pre
                pre = head
                head = tmp
            cur.next = pre
            cur = start
            cur.next = head
        
        return dummy.next
    
    def getLen(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n