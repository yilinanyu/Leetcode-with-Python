def converstlton(stringa):
	dict = {'a': '47', 'b': '2', 'c': '3'}
	res = ""
	for i in range(len(stringa)):
		if stringa[i].isalnum():
			if stringa[i] in dict:
				res = res + dict[stringa[i]]
			else:
				res = res + stringa[i]
		else:
			res = res + stringa[i]
	return res
print converstlton("a1b 2c")
