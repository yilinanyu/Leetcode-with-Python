def isPalindrome(x):
	if x < 0:
		return False
	n = len(str(x))
	l = 0
	r = n -1
	while l < r:
		if str(x)[l] != str(x)[r]:
			return False
		l += 1
		r -= 1
	return True 
print isPalindrome(12211)