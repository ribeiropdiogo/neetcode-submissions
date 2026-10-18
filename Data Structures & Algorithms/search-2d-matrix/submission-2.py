class Solution:

    def searchBinList(self, start: int, end: int, l: List[int], t: int) -> bool:
        partition = start + ((end - start) // 2)
        if l[partition] == t:
            return True
        
        if end - start > 0:
            if l[partition] < t:
                return self.searchBinList(partition+1, end, l, t)
            else:
                return self.searchBinList(start, partition-1, l, t)
        else:
            return False

    def searchBinMatrix(self, start: int, end: int, m: List[List[int]], t: int) -> bool:
        partition = start + ((end - start) // 2)
        
        if m[partition][0] == t:
            return True
        
        if end - start == 1:
            return self.searchBinList(0, len(m[partition])-1, m[partition], t)
        
        
        if m[partition][0] < t and (end - start) > 1:
            return self.searchBinMatrix(partition,end,m,t)
        else:
            return self.searchBinMatrix(start,partition,m,t)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchBinMatrix(0, len(matrix), matrix, target)
        