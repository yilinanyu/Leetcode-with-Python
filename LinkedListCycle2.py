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
        if head is None or head.next is None:
            return None
        slow = fast = head
        while fast and fast.next:
            #注意快慢指针的定义是在本身的基础上，而非head
            slow = slow.next
            fast = fast.next.next
            #并非值相同， 是指针位置一样，故也是== 即快慢指针相遇，存在环路
            if slow == fast:
                break
        # 当他俩相遇以后，fast 指针不动，slow 指针回到head，然后slow and fast 同事向前走，这一次两个都是一次一步，两者相遇的点就是环路的起点。
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
                
        
            
        
        