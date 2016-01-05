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
        # 用快慢指针寻找mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转中点后的list
        p,last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last,p = p,next
        # 判断是否是palindrome
        p1,p2 = last,head
        while p1 and p1.val == p2.val:
            p1,p2 = p1.next,p2.next
        #如果p1 是none，ruturn true
        return p1 is None
            
        