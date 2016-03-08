# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # for every intervals, sort the start integer and end integer
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        s, e = 0,0
        available = 0
        numroom = 0
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    numroom += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e +=1 
        return numroom
                    