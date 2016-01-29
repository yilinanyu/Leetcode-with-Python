def check_Number(lst):
	ans = []
	B = 0
	for i in range(len(lst)):
		B = lst[i] + 1
		if B in range(1,10):
			A2 = B + 1
			if A2 not in range(1,10):pass
			elif abs(A2-lst[i])/lst[i] > 1:pass
			else:ans.append(lst[i])
		else:
			pass
	return ans
print check_Number([1,2,3,4])