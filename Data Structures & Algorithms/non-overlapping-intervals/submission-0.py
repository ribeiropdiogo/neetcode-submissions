class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals
        intervals.sort()
        res, prevEnd = 0, intervals[0][1]

        if len(intervals) > 1:
            for i in range(1,len(intervals)):
                if intervals[i][0] >= prevEnd:
                    prevEnd = intervals[i][1]
                else:
                    prevEnd = min(prevEnd, intervals[i][1])
                    intervals[i][1] = prevEnd
                    res += 1
        
        return res

