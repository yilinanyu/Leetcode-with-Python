# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        return self.compare(head, self.rotate(right))
        
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def rotate(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head 
            head = temp
            
        return pre
    def compare(self, h1, h2):
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True
        
        
        
        