# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        #since we neeed to circle 不断的循环。head 只代表一次
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if id(slow) == id(fast):
                return True
        return False
        