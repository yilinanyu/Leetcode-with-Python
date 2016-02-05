def mergeTwoLists(self, l1, l2):
	# cur is dynamic 
	dummy  = cur = ListNode(0)
	while l1 and l2:
		if l1.val < l2.val:
			cur.next = l1
			l1 = l1.next
			cur = cur.next
		else:
			cur.next = l2
			l2 = l2.next
			cur = cur.next
	if l1:
		cur.next = l1
	if l2:
		cur.next = l2
	return dummy.next
	
