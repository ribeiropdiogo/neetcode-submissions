class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        j = 0


        if len(intervals) > 1:
            for i in range(1,len(intervals)):
                if intervals[i][0] <= res[j][1]:
                    res[j] = [min(intervals[i][0],res[j][0]),max(intervals[i][1],res[j][1])]
                else:
                    res.append(intervals[i])
                    j += 1
        
        return res