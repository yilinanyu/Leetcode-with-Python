"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 0
        while reader.get(index) != -1 and reader.get(index) < target:
            index = index *2 + 1
        start = 0
        end = index
        while start + 1 < end:
            mid = start + (end - start)/2
            if reader.get(mid)>= target:
                end = mid
            else:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1