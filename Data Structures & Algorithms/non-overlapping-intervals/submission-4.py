class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        res = []

        print(intervals)

        for interval in intervals:
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
                continue
                
            elif res[-1][1] > interval[0]:
                if (interval[1] < res[-1][1]):
                    res[-1] = interval
                count += 1
                continue

        return count

            

