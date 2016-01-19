# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge case：
        if head is None or head.next is None:
            return None
        # 定义快慢指针& 运行
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 双等号代表值相等
            if slow == fast:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
            
  