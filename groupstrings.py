import collections
def groupStrings(strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    dic = collections.defaultdict(list)
    for w in strings:
        shift = tuple([(ord(c) - ord(w[0])) % 26 for c in w])
        dic[shift].append(w)
    return map(sorted, dic.values())
#     for key,values in dic.items():
#         print (key,":",values)
#         # print 
# groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])