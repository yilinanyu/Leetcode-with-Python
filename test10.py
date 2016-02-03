def excel(num):
	# number to title
	ans = ''
	while num:
		ans = ans + chr(ord('A')+ (num-1)%26)
		num = (num - 1)/26
	return ans

print excel(27)