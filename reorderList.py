# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head==None or head.next==None or head.next.next==None: return head
        
        # break linked list into two equal length
        slow = fast = head                              #快慢指针技巧
        while fast and fast.next:                       #需要熟练掌握
            slow = slow.next                            #链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy=ListNode(0); dummy.next=head2             #翻转前加一个头结点
        p=head2.next; head2.next=None                   #将p指向的节点一个一个插入到dummy后面
        while p:                                        #就完成了链表的翻转
            tmp=p; p=p.next                             #运行时注意去掉中文注释
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        # merge two linked list head1 and head2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; tmp2 = p2.next
            p1.next = p2; p2.next = tmp1
            p1 = tmp1; p2 = tmp2