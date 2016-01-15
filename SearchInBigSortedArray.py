
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) != -1 and reader.get(index) < target:
            index = index * 2 + 1
        
        start, end = 0, index
        while start + 1 < end:
            mid = (start + end) / 2
            if reader.get(mid) == - 1 or reader.get(mid) >= target:
                end = mid
            else:
                start = mid
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1