def reverseWords(s):
	return ".".join(s.split(".")[::-1])
s = "www.apple.com"
print reverseWords(s)