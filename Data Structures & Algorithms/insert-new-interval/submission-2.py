class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)-1,-1,-1):
            # Insert interval after index if new_start > i_end
            if newInterval[0] > intervals[i][1]:
                intervals.insert(i+1,newInterval)
                newInterval = None
                break
            # Skip if interval is before current interval
            if newInterval[1] < intervals[i][0]:
                continue
            # Check if there is an overlap
            if newInterval[1] >= intervals[i][0] or newInterval[0] <= intervals[i][1]:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
                intervals.pop(i)

        if newInterval is not None:
            intervals.insert(0,newInterval)
        
        return intervals