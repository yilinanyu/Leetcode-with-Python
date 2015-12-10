import collections
import operator
# pattern = "1234"
# secret = "1134"
bull = sum(map(operator.eq, pattern, secret))
p = collections.Counter(pattern)
s = collections.Counter(secret)
# print the values in the dictionary
cow = sum((p&s).values()) - bull
# cow =  sum(map(operator.ne, pattern, secret))
print str(bull) + 'A' + str(cow) + 'B'