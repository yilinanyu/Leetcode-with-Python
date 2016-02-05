class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #collection.defaultdict is used instead of Counter. It is almost same as dict but you can set default value (the value when item is not found in the dictionary)list comprehension is used in the return statement in order to select anagrams which have more than 1 word and also to flatten the d.values() which is list of lists
        dic = collections.defaultdict(list)
        ans = []
        for s in strs:
            dic[str(sorted(s))].append(s)
        for value in dic.values():
            ans.append(sorted(value))
        return ans