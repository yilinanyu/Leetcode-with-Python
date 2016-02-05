class Solution(object):
    # O(N) O(N)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        ans = []
        for s in strs:
            dic[str(sorted(s))].append(s)
        for value in dic.values():
            ans.append(sorted(value))
        return ans