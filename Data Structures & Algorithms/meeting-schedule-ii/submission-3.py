"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals by start time
        # create minheap of end times
        # check if next interval start overlaps with all of end times, in which case add it to heap, else pop
        ends = []

        intervals.sort(key = lambda x: x.start)

        for i in intervals:
            if ends and i.start >= ends[0]:
                heapq.heappop(ends)                    
            heapq.heappush(ends, i.end)



        return(len(ends))
        