import re
def findcourse(str1):
	s = "abc#def#ghi#jkl"
	re.findall(r"(?<=#)[^#]+(?=#)", s)