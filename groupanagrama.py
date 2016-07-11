class Solution(object):
    def groupAnagrams(self, strs):
        line = []
        dict = {}
        for elem in strs:
            sortedelem = "".join(sorted(elem))
            if sortedelem in dict:
                dict[sortedelem] += [elem]
            else:
                dict[sortedelem] = [elem]
        for key, value in dict.iteritems() :
            line.append(sorted(value))
        return line