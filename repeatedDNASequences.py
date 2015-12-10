class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #set '0' as the default value for non-existing keys
        sequences = collections.defaultdict(int)
        for i in range(len(s)):
            #add 1 to the count
            sequences[s[i:i+10]] += 1
        #extract the relevant keys
        return [key for key, value in sequences.iteritems() if value > 1] 