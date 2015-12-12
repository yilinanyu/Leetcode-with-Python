class Solution:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
                pre = dummy                         #直到一个节点的值小于前面节点的值
                while pre.next.val < curr.next.val: #然后寻找插入的位置
                    pre = pre.next
                tmp = curr.next                     #上面的示意图就是以下这段代码
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next